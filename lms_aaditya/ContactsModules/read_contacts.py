from MongoConnect import ConnectModule

my_conn = ConnectModule.connect()
collection = my_conn.db['Contacts']


class ReadContact:
    def __init__(self, reg_id):
        self.reg_id = reg_id

    def read(self):
        return collection.find({"Register Id": self.reg_id})
