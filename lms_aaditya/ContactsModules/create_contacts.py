from MongoConnect import ConnectModule
a = ConnectModule.connect()
collection = a.db["Contacts"]


class CreateContact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def create(self):
        Data = {
            "Name ": self.name,
            "Email ID ": self.email,
            "Phone number ": self.phone
        }

        return collection.insert_one(Data)


