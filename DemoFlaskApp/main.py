from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://myuser:mypassword@localhost/pythondb'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(150))
    author = db.Column(db.String(50))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author


# Create a function to create the tables within an application context
def create_tables():
    with app.app_context():
        # Create the tables in the database
        # Warning to use it cautiously in production environment
        db.create_all()


create_tables()


class PostSchema(ma.Schema):
    class Meta:
        fields = ('title', 'description', 'author')


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


@app.route('/blog', methods=['POST'])
def addBlog():
    title = request.json['title']
    description = request.json['description']
    author = request.json['author']

    new_post = Blog(title, description, author)
    db.session.add(new_post)
    db.session.commit()

    return post_schema.jsonify(new_post)


@app.route('/blog', methods=['GET'])
def getBlogs():
    post_list = Blog.query.all()
    return posts_schema.jsonify(post_list)


@app.route('/blog/<int:b_id>', methods=['GET'])
def getBlog(b_id):
    post = db.session.get(Blog, b_id)
    return post_schema.jsonify(post)


@app.route('/blog/<int:b_id>', methods=['PUT'])
def updateBlog(b_id):
    post = db.session.get(Blog, b_id)

    title = request.json['title']
    description = request.json['description']
    author = request.json['author']

    post.title = title
    post.description = description
    post.author = author

    db.session.commit()

    return post_schema.jsonify(post)


@app.route('/blog/<int:b_id>', methods=['DELETE'])
def deleteBlog(b_id):
    post = db.session.get(Blog, b_id)
    db.session.delete(post)
    db.session.commit()

    return post_schema.jsonify(post)


@app.route('/welcome', methods=['GET'])  # by default uses get as methods
def welcome():
    return render_template("welcome.html", name="user")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
