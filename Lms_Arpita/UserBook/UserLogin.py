from bson import ObjectId

from Lms_Arpita.DatabaseConnectivity import MongoConnection

p = MongoConnection.path()
collection = p.db["UserLogBook"]


class User:
    def create_user(self, user_name, email_id, password, age, gender):
        user_details = {
            "Name": user_name,
            "Email_id": email_id,
            "Password": password,
            "Age": age,
            "Gender": gender,
        }
        return collection.insert_one(user_details)

    def login(self, user_id, password):
        myquery = {"Email_id": {"$eq": user_id}, "Password": {"$eq": password}}
        access = collection.find_one(myquery)
        if access is None:
            print("access denied plz check ur id and password")
        else:
            print("welcome now u have access to ur data")
            # give info of user

    def getId(self, object_id, password):
        compare = collection.find_one({"Email_id": object_id, "Password":  password})
        uniqueid = compare["_id"]
        return uniqueid


    def delete_user(self, object_id):
        return collection.delete_one({"_id": ObjectId(object_id)})

    def update_user(self, object_id, user_data):
        return collection.update_one({"_id": ObjectId(object_id)}, {"$set": user_data})








