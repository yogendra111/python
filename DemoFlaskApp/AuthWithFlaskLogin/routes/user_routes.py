from flask import request, jsonify, make_response
from flask_login import login_user, logout_user

from AuthWithFlaskLogin import app, db
from AuthWithFlaskLogin.models import User
from AuthWithFlaskLogin.serializers import userSchema


# Creates a user loader callback that returns the user object given an id
# @login_Manager.user_loader
# def loader_user(user_id):
#     return User.query.get(user_id)


@app.route('/register', methods=["POST"])
def register():
    user = User(username=request.json['username'], password=request.json['password'])
    db.session.add(user)
    db.session.commit()
    return userSchema.jsonify(user)


@app.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(username=request.json["username"]).first()
    if user.password == request.json["password"]:
        login_user(user)
        return make_response(jsonify({"response": "User Logged in"}), 200)
    return make_response(jsonify({"error": "User not register"}), 401)


@app.route("/logout")
def logout():
    logout_user()
    return make_response(jsonify({"response": "User Logged out"}), 200)