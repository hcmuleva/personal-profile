from bson import ObjectId

from Lms_Arpita.DatabaseConnectivity import MongoConnection
p = MongoConnection.path()
collection = p.db["ContactBook"]

class Contacts:
    def create_contact(self, object_id, user_name, phone_no):
        contact_details = {
            "object_id": object_id,
            "name": user_name,
            "phone_number": phone_no
        }
        return collection.insert_one(contact_details)

    def get_contact(self, object_id):
        print(collection.find_one({"object_id": object_id}))

    def delete_contact(self, contact_id):
        return collection.delete_one({"_id": ObjectId(contact_id)})

    def update_contact(self, contact_id, contact_data):
        return collection.update_one({"_id": ObjectId(contact_id)}, {"$set": contact_data})

    def getId(self, user_name):
        compare = collection.find_one({"user name": user_name})
        if compare is None:
            print("plz check ur id and password")
        else:
            uniqueid = compare["_id"]
            return uniqueid