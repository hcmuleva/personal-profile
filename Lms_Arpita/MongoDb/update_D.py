from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['lms_db']
collection = db['student_data']
data = {
    'name': 'arpi',
    'class': 14,
    'result': '100 pecent'
}
new_data = {
    "$set": {
    'name': 'aadi',
    'class': 4,
    'result': '0 pecent'
    }
}
collection.update_one(data,new_data)
print("updated")