from flask import session
def authenticateUser(database, userName: str, password: str):
    userData = database.users.find_one({'username': userName})
    if userData and userData['password'] == password:
        session['userId'] = userData.userId
    
