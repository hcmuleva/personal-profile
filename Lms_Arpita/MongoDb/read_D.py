from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['lms_db']
collection = db['student_data']
print(collection.find_one())