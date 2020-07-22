from MongoConnect import ConnectModule
my_con = ConnectModule.connect()
collection = my_con.db["Personal_details"]


class UpdateDetails:
    def __init__(self, up_reg_id, up_blood_grp, up_academics, up_fname, up_mname, up_hobbies):
        self.up_reg_id = up_reg_id
        self.up_blood_grp = up_blood_grp
        self.up_academics = up_academics
        self.up_fname = up_fname
        self.up_mname = up_mname
        self.up_hobbies = up_hobbies

    def update_details(self):
        updated_data = {"$set": {
            "Registration Id": self.up_reg_id,
            "Blood group": self.up_blood_grp,
            "Academics": self.up_academics,
            "Fathers name": self.up_fname,
            "Mothers name": self.up_mname,
            "Hobbies": self.up_hobbies
            }
        }
        return collection.update({"Registration Id": self.up_reg_id}, updated_data)
