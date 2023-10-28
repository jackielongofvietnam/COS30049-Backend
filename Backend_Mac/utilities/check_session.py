from functools import wraps
from flask import session
from utilities.response import response

def check_session():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not session:
                return response(401, "No session found or session expired! Please log in again.")
            return func(*args, **kwargs)

        return wrapper

    return decorator