from MongoConnect import ConnectModule
a = ConnectModule.connect()
collection = a.db["Address"]


class CreateAddress:
    def __init__(self, register_id, house_num, street, city, district, state, pincode):
        self.register_id = register_id
        self.house_num = house_num
        self.street = street
        self.city = city
        self.district = district
        self.state = state
        self.pincode = pincode

    def create_add(self):
        data = {
            "Register Id": self.register_id,
            "House number ": self.house_num,
            "Street ": self.street,
            "City ": self.city,
            "District": self.district,
            "State": self.state,
            "Pin Code": self.pincode
        }

        return collection.insert_one(data)
