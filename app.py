from flask import Flask, request
from flask_cors import CORS, cross_origin
from modules.audit import audit_smart_contract
from modules.audit_history import search_audit_history
from modules.auth import authenticate_user
from data_access.mongodb_connection import connect_mongodb
from utilities.response import response
from utilities.check_token import check_token


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADER'] = 'Content-Type' 
app.config['SECRET_KEY'] = 'smartcontractauditsystem123'
db = connect_mongodb()


@app.route("/api/login", methods=['POST'])
@cross_origin(origins='*')
def login():
    if db == None:
        return response(503, 'DB connection failed! Please try again later')
    data = request.json
    user_name = data.get('user_name')
    password = data.get('password')

    return authenticate_user(db, app, user_name, password)


@app.route("/api/audit", methods=['POST'])
@check_token(app)
def audit():
    
    if db == None:
        return response(503, 'DB connection failed! Please try again later')
    data = request.json
    file_name = data.get('file_name')
    file_content = data.get('file_content')

    return audit_smart_contract(db, file_name, file_content)


@app.route("/api/audit-history", methods=['GET'])
@check_token(app)
def audit_history():    
    if db == None:
        return response(503, 'DB connection failed! Please try again later')
    data = request.args
    search = data.get('search')

    return search_audit_history(db, search)


if __name__ == '__main__':
    app.run()
