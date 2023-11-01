from uuid import uuid4
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://myuser:mypassword@localhost/pythondb"
app.config['SECRET_KEY'] = "998a0c50bb4a6240e9c83f7cc713d46ea6ca2f91c2a45b54a6d5c3cf61aa005e"
db = SQLAlchemy(app)
ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'username', 'password', 'role')


userSchema = UserSchema()
usersSchema = UserSchema(many=True)


class BlogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date')


blogSchema = BlogSchema()
blogsSchema = BlogSchema(many=True)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), default='user')

    def __repr__(self):
        return f'<User {self.id} {self.username}>'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return f'<Blog(id={self.id}, title={self.title}, description={self.description}, date={self.date})>'


with app.app_context():
    db.create_all()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # if 'x-access-token' in request.headers: # for custom header
        #     token = request.headers['x-access-token']
        if 'Authorization' in request.headers:
            if "Bearer" in request.headers['Authorization']:
                token = request.headers['Authorization'][7:]

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except Exception as e:
            return jsonify({"error": f"Token is invalid {e}"}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json();

    hash_password = generate_password_hash(data['password'])
    new_user = User(public_id=str(uuid4()), username=data['username'], password=hash_password, role=data['role'])
    db.session.add(new_user)
    db.session.commit()

    return userSchema.jsonify(new_user)


@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if current_user.role != 'admin':
        return jsonify({'error':"you don't have admin access"})

    users = User.query.all()
    return usersSchema.jsonify(users)


@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if current_user.role != 'admin':
        return jsonify({'error':"you don't have admin access"})
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({"error": "no user Found!"})
    return userSchema.jsonify(user)


@app.route('/user/<string:public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({"error": "no user Found!"})

    db.session.delete(user)
    db.session.commit()
    return jsonify({"Deleted user": {"public_id": user.public_id, "usrename": user.username}})


@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    user = User.query.filter_by(username=auth.username).first();

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    if not check_password_hash(user.password, auth.password):
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    token = jwt.encode({'public_id': user.public_id, 'exp': datetime.utcnow() + timedelta(days=1)},
                       app.config['SECRET_KEY']) # timedelta(minutes=30)
    return jsonify({'token': token})


@app.route('/blog', methods=['POST'])
@token_required
def add_blog(current_user):
    data = request.get_json()
    new_blog = Blog(title=data['title'], description=data['description'])
    db.session.add(new_blog)
    db.session.commit()
    return blogSchema.jsonify(new_blog)


@app.route('/blog', methods=['GET'])
@token_required
def get_all_blogs(current_user):
    blogs = Blog.query.all()
    return blogsSchema.jsonify(blogs)


@app.route('/blog/<blog_id>', methods=['GET'])
@token_required
def get_blog(current_user, blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    if not blog:
        return jsonify({"error": f"no blog found with id = {blog_id}"}), 404

    return blogSchema.jsonify(blog)


@app.route('/blog/<int:blog_id>', methods=['DELETE'])
@token_required
def delete_blog(current_user, blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    if not blog:
        return jsonify({"error": f"no blog found with id = {blog_id}"}), 404

    db.session.delete(blog)
    db.session.commit()
    return jsonify({"Deleted blog": {"id": blog.id, "title": blog.title}})


if __name__ == '__main__':
    app.run(debug=True)
