from Lms_Arpita.DatabaseConnectivity import MongoConnection
p = MongoConnection.path()
collection = p.db["AdressBook"]


class User_address:
    def create_address(self, user_id, house_no, house_name, street_name, city_name, pincode):
        address_details ={
            "user_id": user_id,
            "house_No": house_no,
            "house_Name": house_name,
            "street_Name": street_name,
            "city_Name": city_name,
            "pincode": pincode
        }
        return collection.insert_one(address_details)
    def get_all_addresses(self,user_id):
        return collection.find_many({"user_id":user_id})
    def delete_address(self,address_id ):
        return collection.delete_one({"_id",address_id})
    def update_address(self,address_id, address_data):
        return collection.update_one({"_id":address_id},{"$set":address_data})
