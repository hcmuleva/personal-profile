from test_module import mongoConnection

p = mongoConnection.path()
collection = p.db["userDetails"]


class Detail:

    def createUser(self ,userName, userId,password,age, location):
        user_info = {
            "Name": userName,
            "Id": userId,
            "Password": password,
            "Age": age,
            "Location": location
        }
        return collection.insert_one(user_info)

    def autheticateUser(self, UserId, Password):
        userData=collection.find_one({"Id":UserId, "Password":Password})
        isAuthenticated=False
        if None == userData:
            isAuthenticated=False
            print("Authentication failed")
        else:
            isAuthenticated=True
        return isAuthenticated