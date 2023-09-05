import jwt
import datetime
from functools import wraps
from flask import request, jsonify


secret_key = "ENTER YOUR SECRET CODE"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            token = token.replace('Bearer ', '')
            data = jwt.decode(token, secret_key, algorithms=['HS512'])
            # Menambahkan user_id ke dalam request
            request.user_id = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        return f(data, *args, **kwargs)
    return decorated


def generate_token(user_id: str):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        "iat": datetime.datetime.utcnow(),
    }
    token = jwt.encode(payload, secret_key, algorithm="HS512")
    return token.decode("utf-8")




