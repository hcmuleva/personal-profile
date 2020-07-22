from Lms_Arpita.UserBook.UserLogin import User
from Lms_Arpita.DatabaseConnectivity import MongoConnection
p = MongoConnection.path()
collection = p.db["addressBook"]

get_id = input("Enter Id:")
get_password = input("Enter Password:")
print(get_password)
myobj = User()
myobjecid= myobj.getId(get_id, get_password)
print(myobjecid)

