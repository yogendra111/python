from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify, make_response

from AuthAPIs import app, db, auth
from AuthAPIs.models import User
from AuthAPIs.serializers import userSchema


@app.route('/register', methods=["POST"])
def register():
    user = User(username=request.json['username'],
                password=generate_password_hash(request.json['password'], method='pbkdf2:sha256'))
    db.session.add(user)
    db.session.commit()
    return userSchema.jsonify(user)


# verify credential for login required endpoint
@auth.verify_password
def verify(username, password):
    if not username or not password:
        return False

    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            return username

