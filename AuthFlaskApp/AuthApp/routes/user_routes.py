from AuthApp import app, db
from AuthApp.modals import User
from AuthApp.serializers import userSchema, usersSchema
from AuthApp.decorators import token_required

from flask import request, jsonify
from werkzeug.security import generate_password_hash
from uuid import uuid4


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    hash_password = generate_password_hash(data['password'])
    new_user = User(public_id=str(uuid4()), username=data['username'], password=hash_password, role=data['role'])
    db.session.add(new_user)
    db.session.commit()

    return userSchema.jsonify(new_user)


@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if current_user.role != 'admin':
        return jsonify({'error': "you don't have admin access"})

    users = User.query.all()
    return usersSchema.jsonify(users)


@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if current_user.role != 'admin':
        return jsonify({'error': "you don't have admin access"})
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
