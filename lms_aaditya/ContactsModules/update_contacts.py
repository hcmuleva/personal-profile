from MongoConnect import ConnectModule
from bson.objectid import ObjectId
my_con = ConnectModule.connect()
collection = my_con.db["Contacts"]


class UpdateContact:
    def __init__(self, uname, uemail, uphone, doc_id):
        self.uname = uname
        self.uemail = uemail
        self.uphone = uphone
        self.doc_id = doc_id

    def update(self):
        newdata = {"$set": {
            "Name ": self.uname,
            "Email ID ": self.uemail,
            "Phone number ": self.uphone
          }
        }
        return collection.update({"_id": ObjectId(self.doc_id)}, newdata)
