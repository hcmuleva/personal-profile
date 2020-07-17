from pymongo import MongoClient
class MyDB:
    def __init__(self):
        pass
    def getconnection(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['lms_db']
        return db

