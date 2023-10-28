from flask import session, jsonify
from utilities.response import response

def authenticate_user(database, username, password):
    user_data = database.Users.find_one({'username': username})
    if user_data and user_data['password'] == password:
        session['user_id'] = str(user_data['_id'])
        return_data = {"username": user_data['username']}
        return response(200, "Login successful!", return_data)
    else:
        return response(401, "Login failed! Wrong username or password")
