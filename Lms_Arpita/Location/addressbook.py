from bson import ObjectId

from Lms_Arpita.DatabaseConnectivity import MongoConnection

p = MongoConnection.path()
collection = p.db["AdressBook"]


class User_address:
    def create_address(self, object_id, house_no, house_name, street_name, city_name, pincode):
        address_details = {
            "object_id": object_id,
            "house_No": house_no,
            "house_Name": house_name,
            "street_Name": street_name,
            "city_Name": city_name,
            "pincode": pincode
        }
        return collection.insert_one(address_details)

    def get_addresses(self, object_id):
        print(collection.find_one({"user_id": object_id}))

    def delete_address(self, address_id):
        return collection.delete_one({"_id": ObjectId(address_id)})

    def update_address(self, address_id, address_data):
        return collection.update_one( {"_id": ObjectId(address_id)},{"$set": address_data})
    def getAddressId(self, object_id):
        compare = collection.find_one({"object_id": object_id})
        uniqueid = compare["_id"]
        return uniqueid




