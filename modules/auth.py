from flask import session
from utilities.response import response
from data_access.users import find_user_by_username

def authenticate_user(db, user_name, password):
    user = find_user_by_username(db, user_name)

    if user and user['password'] == password:
        session['user_id'] = str(user['_id'])
        print(session)
        return_data = {"user_name": user['user_name']}
        return response(201, "Login successful!", return_data)
    else:
        return response(401, "Login failed! Wrong username or password")
