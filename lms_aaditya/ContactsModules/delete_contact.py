from MongoConnect import ConnectModule
from bson.objectid import ObjectId
a = ConnectModule.connect()
collection = a.db['Contacts']


class DeleteContact:
    def __init__(self, obj_id):
        self.obj_id = obj_id

    def delete(self):
        return collection.remove({"_id": ObjectId(self.obj_id)})
