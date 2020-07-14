from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['lms_db']
collection = db['contacts']

name = input("Enter your name : ")
mail = input("Enter your E-Mail ID : ")
phone = int(input("Enter your contact number : "))

data = {
    "Name ": name,
    "E-mail ": mail,
    "Contact Number ": phone
}


collection.delete(data)

