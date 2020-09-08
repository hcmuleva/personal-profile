from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['lms_db']
collection = db["TestContacts"]

uid = "temp"


class TestCreateContact:
    def test_create(self):
        global uid
        my_data = {
            "name": "harish",
            "last_name": "Muleva"
        }
        uid = collection.insert_one(my_data).inserted_id
        assert uid is not None
        # test passed
