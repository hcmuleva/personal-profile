from MongoConnect import ConnectModule
from bson.objectid import ObjectId
mycon = ConnectModule.connect()
collection = mycon.db["UserLogin"]


class User:
    def register(self, user_name, user_pass, user_age, user_gender):
        register_user = {
            "User Name ": user_name,
            "Password ": user_pass,
            "Age ": user_age,
            "Gender ": user_gender
        }
        return collection.insert_one(register_user)

    def user_login(self, user_name, user_pass):
        user_data = collection.find_one({"User Name ": user_name, "Password ": user_pass})
        is_authenticated = False
        if None == user_data:
            is_authenticated = False
            print("Authentication failed")

        else:
            is_authenticated = True
            return "You are logged in"
