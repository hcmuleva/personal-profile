from MongoConnect import ConnectModule
from bson.objectid import ObjectId
a = ConnectModule.connect()
collection = a.db['Contacts']


class DeleteContact:
    def __init__(self, reg_id):
        self.reg_id = reg_id

    def delete(self):
        return collection.remove({"_id": ObjectId(self.reg_id)})
