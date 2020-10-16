from MongoConnect import ConnectModule
conn = ConnectModule.connect()
collection = conn.db["Personal_details"]


class PersonalDetails:
    def __init__(self, reg_id, blood_grp, academics, fname, mname, hobbies):
        self.reg_id = reg_id
        self.blood_grp = blood_grp
        self.academics = academics
        self.fname = fname
        self.mname = mname
        self.hobbies = hobbies

    def details(self):
        data = {
            "Registration Id": self.reg_id,
            "Blood group": self.blood_grp,
            "Academics": self.academics,
            "Fathers name": self.fname,
            "Mothers name": self.mname,
            "Hobbies": self.hobbies
        }
        return collection.insert_one(data)
