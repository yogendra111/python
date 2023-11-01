from . import app
from .modals import User

from functools import wraps
from flask import request, jsonify
import jwt


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
