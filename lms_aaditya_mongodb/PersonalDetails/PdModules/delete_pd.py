from MongoConnect import ConnectModule
conn = ConnectModule.connect()
collection = conn.db["Personal_details"]


class DeleteDetails:
    def __init__(self, reg_id):
        self.reg_id = reg_id

    def delete_details(self):
        return collection.remove({"Registration Id": self.reg_id})
