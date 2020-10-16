from MongoConnect import ConnectModule
conn = ConnectModule.connect()
collection = conn.db["Personal_details"]

"""
Instructions ---
type 1 - get all data using registration id
type 2 - get document which must have both item 1 and item 2 
type 3 - get document which have items in common 
type 4 - get document which have any of item 1 or item 2 
type 5 - get document which have neither item 1 nor item 2 
"""


class ReadDetails:
    def __init__(self, reg_id):
        self.reg_id = reg_id

    def read_details(self):
        return collection.find({"Registration Id": self.reg_id})

