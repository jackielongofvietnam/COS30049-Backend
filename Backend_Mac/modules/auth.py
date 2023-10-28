from flask import session
from utilities.response import response

def authenticateUser(database, userName: str, password: str):
    userData = database.Users.find_one({'userName': userName})
    if userData and userData['password'] == password:
        session['userId'] = str(userData['_id'])
        print(session)
        return response(200, "Login successful!")
    else:
        return response(401, "Login failed! Wrong username or password")
