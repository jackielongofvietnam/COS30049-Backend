from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from modules.audit import auditSmartContract
import certifi

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADER'] = 'Content-Type' 



@app.route("/api/login", methods=['POST'])
@cross_origin(origins='*')
def login():
    data = request.json
    
    userName = data.get('userName')
    password = data.get('password')
    
    #URL
    url = "mongodb+srv://"+userName+":"+password+"@testcluster.7phucdo.mongodb.net/?retryWrites=true&w=majority"
    
    # Create a new client and connect to the server
    client = MongoClient(url, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    # Send a ping to confirm a successful connection
    try:
        client.Audit.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return jsonify({'status': 'success', 'message': 'Connection to MongoDB server successful'})
    except Exception as e:
        return jsonify({'status': 'failure', 'message': 'Connec totion MongoDB server failed:'})


@app.route("/api/audit", methods=['GET'])
def audit():
    data = request.json
    fileName = data.get('fileName')
    fileContent = data.get('fileContent')

    return auditSmartContract(fileName, fileContent)



if __name__ == '__main__':
    app.run()
