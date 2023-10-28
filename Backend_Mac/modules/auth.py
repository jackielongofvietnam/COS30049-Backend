from flask import session
from utilities.response import response

def authenticate_user(database, username, password):
    user_data = database.Users.find_one({'userName': username})
    if user_data and user_data['password'] == password:
        session['user_id'] = str(user_data['_id'])
        session.permanent = True
        return response(200, "Login successful!")
    else:
        return response(401, "Login failed! Wrong username or password")
