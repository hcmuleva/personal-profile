from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['lms_db']

collection = db['test-collection']

post = {"author": "Mike",
       "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": "good"}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
