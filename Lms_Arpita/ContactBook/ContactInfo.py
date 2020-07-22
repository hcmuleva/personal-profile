from Lms_Arpita.DatabaseConnectivity import MongoConnection
p = MongoConnection.path()
collection = p.db["ContactBook"]

class Contacts:
    def create_contact(self, user_id, user_name, phone_no ):
        contact_details = {
            "user_id": user_id,
            "name": user_name,
            "phone_number": phone_no
        }
        return collection.insert_one(contact_details)