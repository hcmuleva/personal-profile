from Lms_Arpita.DatabaseConnectivity import MongoConnection

p = MongoConnection.path()
collection = p.db["UserLogBook"]


class User:
    def create_user(self, user_name, user_id, password, age, gender):
        user_details = {
            "Name": user_name,
            "Email_id": user_id,
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

    def getId(self, user_id, password):
        compare = collection.find_one({"Email_id": user_id, "Password":  password})
        if compare is None:
            print("plz check ur id and password")
        else:
            uniqueid = compare["_id"]
            return uniqueid


    # def update_user(self,
    #                 ):








