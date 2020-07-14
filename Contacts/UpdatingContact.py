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

new_name = input("Enter your new name : ")
new_mail = input("Enter your new E-Mail ID : ")
new_phone = int(input("Enter your new contact number : "))

new_data = {"$set": {
    "Name ": new_name,
    "E-mail ": new_mail,
    "Contact Number ": new_phone
    }
}
collection.update_one(data, new_data)
print("Contact updated")
