from MongoConnect import ConnectModule

my_conn = ConnectModule.connect()
collection = my_conn.db['Address']


class ReadAddress:
    def __init__(self, reg_id):
        self.reg_id = reg_id

    def read_add(self):
        return collection.find({"Register Id": self.reg_id})
