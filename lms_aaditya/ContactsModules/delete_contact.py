from MongoConnect import ConnectModule
a = ConnectModule.connect()
collection = a.db['Contacts']


class DeleteContact:
    def __init__(self, reg_id):
        self.reg_id = reg_id

    def delete(self):
        return collection.remove({"Register Id": self.reg_id})
