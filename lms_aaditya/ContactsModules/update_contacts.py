from MongoConnect import ConnectModule
my_con = ConnectModule.connect()
collection = my_con.db["Contacts"]


class UpdateContact:
    def __init__(self, reg_id, uname, uemail, uphone):
        self.uname = uname
        self.uemail = uemail
        self.uphone = uphone
        self.reg_id = reg_id

    def update(self):
        newdata = {"$set": {
            "Registration Id": self.reg_id,
            "Name ": self.uname,
            "Email ID ": self.uemail,
            "Phone number ": self.uphone
          }
        }
        return collection.update({"Registration Id": self.reg_id}, newdata)
