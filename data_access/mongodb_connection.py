from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi


def connect_mongodb():
    username = 'admin'
    password = '3svXKtSqRKd8pP8'
    database = 'Audit'

    #URI
    uri = "mongodb+srv://"+username+":"+password+"@testcluster.7phucdo.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

    # Send a ping to confirm a successful connection
    try:
        client[database].command('ping')
        print("Successfully connected to MongoDB!")
        return client[database]
    except Exception as e:
        print("Failed to connected to MongoDB!")
        print(e)