from flask import session
from utilities.response import response
from data_access.users import find_user_by_username

def authenticate_user(database, username, password):
    user = find_user_by_username(database, username)

    if user and user['password'] == password:
        session['user_id'] = str(user['_id'])
        return_data = {"username": user['username']}
        return response(200, "Login successful!", return_data)
    else:
        return response(401, "Login failed! Wrong username or password")
