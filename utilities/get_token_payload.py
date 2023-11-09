from flask import request
import jwt

def get_token_payload(app):
    token = request.headers.get('Authorization')
    payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

    return payload
