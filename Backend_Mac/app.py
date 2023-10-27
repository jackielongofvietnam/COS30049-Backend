from flask import Flask, request
from flask_cors import CORS, cross_origin
from modules.audit import auditSmartContract
from data_access.mongodb_connection import connectMongoDB

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADER'] = 'Content-Type' 
connectMongoDB()


@app.route("/api/login", methods=['POST'])
@cross_origin(origins='*')
def login():
    data = request.json
    
    userName = data.get('userName')
    password = data.get('password')


@app.route("/api/audit", methods=['GET'])
def audit():
    data = request.json
    fileName = data.get('fileName')
    fileContent = data.get('fileContent')

    return auditSmartContract(fileName, fileContent)



if __name__ == '__main__':
    app.run()
