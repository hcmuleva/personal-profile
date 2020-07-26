from pymongo import MongoClient
#import pprint

client = MongoClient('mongodb://localhost:27017/')
db = client['lms_db']
collection = db['Brands']

"""
post = {"author": "Mike",
       "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": "good"}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
"""
"""
# Inserting document into the database
car_brands = {
    "Santro" : "Hyundai",
    "Terrano" : "Nissan",
    "Desire" : "Swift",
    "creta" : "Honda"
}

Brands = db.Brands
Brands.insert_one(car_brands)
# print(Brand_id)
"""

# Reading the document from the database
# pprint.pprint(Brands.find_one())
# pprint.pprint(Brands.find_one({"Terrano" : "Nissan"}))

"""
# Updating a document
car_brands = {
    "Santro" : "Hyundai",
    "Terrano" : "Nissan",
    "Desire" : "Swift",
    "creta" : "Honda"
}

new_brands = {"$set": {
    "Micra" : "Nissan",
    }
}
collection.update_one(car_brands, new_brands)
for i in collection.find():
    print(i)
"""


"""
# Deleting a document
car_brands = {
    "Santro" : "Hyundai",
    "Terrano" : "Nissan",
    "Desire" : "Swift",
    "creta" : "Honda"
}
collection.delete_one(car_brands)
"""