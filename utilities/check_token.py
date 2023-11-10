from functools import wraps
from flask import request
from utilities.response import response
import jwt
    
def check_token(app):
    """
    A decorator that authenticates the JWT token of every Requests entering endpoint and block any traffic having no token or invalid token
    """
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return response(401, "No token found!")
            try:
                jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return response(403, "Token has expired!")
            except jwt.InvalidTokenError:
                return response(403, "Invalid token!")
            return func(*args, **kwargs)

        return wrapper

    return decorator