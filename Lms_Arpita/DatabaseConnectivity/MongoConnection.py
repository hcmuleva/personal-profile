from pymongo import MongoClient


def path():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['UserBook']
    return db
