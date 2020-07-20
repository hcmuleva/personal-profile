from MongoConnect import ConnectModule
a = ConnectModule.connect()
collection = a.db["Contacts"]


class CreateContact:

    def __init__(self, register_id, name, email, phone):
        self.register_id = register_id
        self.name = name
        self.email = email
        self.phone = phone

    def create(self):
        data = {
            "Register Id": self.register_id,
            "Name ": self.name,
            "Email ID ": self.email,
            "Phone number ": self.phone
        }

        return collection.insert_one(data)
