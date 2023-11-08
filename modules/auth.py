from utilities.response import response
from data_access.users import find_user_by_username
import jwt

def authenticate_user(db, app, user_name, password):
    user = find_user_by_username(db, user_name)

    if user and user['password'] == password:
        payload = {"user_id": str(user['_id'])}
        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        return_data = {"token": token}
        return response(201, "Login successful!", return_data)
    else:
        return response(401, "Login failed! Wrong username or password")
