from datetime import timedelta
from flask import Flask, session, request
from flask_cors import CORS, cross_origin
from modules.audit import auditSmartContract
from modules.auth import authenticateUser
from data_access.mongodb_connection import connectMongoDB
from utilities.response import response

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADER'] = 'Content-Type' 
app.secret_key = 'smartcontractauditsystem123'
app.permanent_session_lifetime = timedelta(minutes=1)
database = connectMongoDB()


@app.route("/api/login", methods=['POST'])
@cross_origin(origins='*')
def login():
    if database == None:
        return response(503, 'Database connection failed! Please try again later')
    data = request.json
    userName = data.get('userName')
    password = data.get('password')

    return authenticateUser(database, userName, password)

@app.route("/api/logout", methods=['POST'])
def logout():
    session.clear()
    return response(200, "Logout successful!")

@app.route("/api/audit", methods=['GET'])
def audit():
    data = request.json
    fileName = data.get('fileName')
    fileContent = data.get('fileContent')

    return auditSmartContract(fileName, fileContent)



if __name__ == '__main__':
    app.run()
