from MongoConnect import ConnectModule
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
        ins = collection.insert_one(register_user).inserted_id
        print("your register Id id - ", ins)

    def user_login(self, user_name, user_pass):
        return collection.find_one({"User Name ": user_name, "Password ": user_pass})
