from MongoConnect import ConnectModule
my_con = ConnectModule.connect()
collection = my_con.db["Contacts"]


class UpdateContact:
    def __init__(self, uname, uemail, uphone, reg_id):
        self.uname = uname
        self.uemail = uemail
        self.uphone = uphone
        self.reg_id = reg_id

    def update(self):
        newdata = {"$set": {
            "Name ": self.uname,
            "Email ID ": self.uemail,
            "Phone number ": self.uphone
          }
        }
        return collection.update({"Register Id": self.reg_id}, newdata)
