from Lms_Arpita.UserBook.UserLogin import UserLogin1
from Lms_Arpita.DatabaseConnectivity import MongoConnection
p = MongoConnection.path()
collection = p.db["addressBook"]

get_id = input("Enter Id:")
get_password = input("Enter Password:")
print(get_password)
myobj = UserLogin1()
myobjecid= UserLogin1.getId(get_id, get_password)
print(myobjecid)

def()