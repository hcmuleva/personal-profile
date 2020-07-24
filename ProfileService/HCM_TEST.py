import os
print(os. getcwd())
from Lms_Arpita.UserBook.UserLogin import User

myuser = User()
get_id = input("Enter Email Id:")
get_password = input("Enter password:")
get_info = myuser.login(get_id, get_password)
print("Login info ",get_info)