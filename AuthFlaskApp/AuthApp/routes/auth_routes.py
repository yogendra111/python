from AuthApp import app
from AuthApp.modals import User

from flask import request, make_response, jsonify
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta


@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    if not check_password_hash(user.password, auth.password):
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    token = jwt.encode({'public_id': user.public_id, 'exp': datetime.utcnow() + timedelta(days=1)},
                       app.config['SECRET_KEY'])  # timedelta(minutes=30)
    return jsonify({'token': token})
