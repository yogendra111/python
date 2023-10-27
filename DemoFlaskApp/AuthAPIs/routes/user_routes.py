from flask import request, jsonify, make_response

from AuthAPIs import app, db
from AuthAPIs.models import User
from AuthAPIs.serializers import userSchema


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
        # login function
        return make_response(jsonify({"response": "User Logged in"}), 200)
    return make_response(jsonify({"error": "User not register"}), 401)


@app.route("/logout")
def logout():
    # logout function
    return make_response(jsonify({"response": "User Logged out"}), 200)