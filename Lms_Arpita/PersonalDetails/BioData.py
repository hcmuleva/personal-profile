from Lms_Arpita.DatabaseConnectivity import MongoConnection

p = MongoConnection.path()
collection = p.db["PersonalDetails"]


class Bio:
    def create_bio(self, object_id, parents_name, siblings_name, blood_group, hobbies):
        bio_details = {
            "object_id": object_id,
            "parents_name": parents_name,
            "siblings_name": siblings_name,
            "blood_group": blood_group,
            "hobbies": hobbies
        }
        return collection.insert_one(bio_details)

    def get_bio(self, object_id):
        return collection.find_one(object_id)
