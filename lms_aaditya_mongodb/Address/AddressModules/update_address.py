from MongoConnect import ConnectModule
my_con = ConnectModule.connect()
collection = my_con.db["Address"]


class UpdateAddress:
    def __init__(self, up_register_id, up_house_num, up_street, up_city, up_district, up_state, up_pincode):
        self.up_register_id = up_register_id
        self.up_house_num = up_house_num
        self.up_street = up_street
        self.up_city = up_city
        self.up_district = up_district
        self.up_state = up_state
        self.up_pincode = up_pincode

    def update_add(self):
        newdata = {"$set": {
            "House number ": self.up_house_num,
            "Street ": self.up_street,
            "City ": self.up_city,
            "District": self.up_district,
            "State": self.up_state,
            "Pin Code": self.up_pincode
            }
        }
        return collection.update({"Registration Id": self.up_register_id}, newdata)
