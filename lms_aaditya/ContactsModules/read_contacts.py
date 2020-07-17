from MongoConnect import ConnectModule
from bson.objectid import ObjectId

my_conn = ConnectModule.connect()
collection = my_conn.db['Contacts']


class ReadContact:
    def __init__(self, object_id):
        self.object_id = object_id

    def read(self):
        return collection.find({"_id": ObjectId(self.object_id)})
