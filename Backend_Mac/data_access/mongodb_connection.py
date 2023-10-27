from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi


def connectMongoDB():
    userName = 'user1'
    password = '31312'

    #URL
    url = "mongodb+srv://"+userName+":"+password+"@testcluster.7phucdo.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(url, server_api=ServerApi('1'), tlsCAFile=certifi.where())

    # Send a ping to confirm a successful connection
    try:
        client.Audit.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print("Failed to connected to MongoDB!")