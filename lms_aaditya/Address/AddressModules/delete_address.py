from MongoConnect import ConnectModule
conn = ConnectModule.connect()
collection = conn.db['Address']


class DeleteAddress:
    def __init__(self, reg_id):
        self.reg_id = reg_id

    def delete_add(self):
        return collection.remove({"Registration Id": self.reg_id})
