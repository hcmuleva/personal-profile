from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('mongodb://localhost:27017/')
db = client['lms_db']
collection = db['student_data']
data = {
    'name': 'aadi',
    'class': 4,
    'result': '0 pecent'
    }

mydeletedItem=collection.delete_one({"_id" : ObjectId("5f0ec26874a531c876bc07bd")})
print(mydeletedItem)