from Lms_Arpita.UserBook.UserLogin import User


myuser = User()
get_in = input("Already signed up? yes/no:")

if get_in == "yes":
    get_id = input("Enter userId:")
    get_password = input("Enter password:")
    get_info = myuser.login(get_id, get_password)
elif get_in == "no":
    print("Kindly fill the given details")
    get_name = input("Enter user_name:")
    get_id = input("Enter user_id:")
    get_password = input("Enter password:")
    get_age = input("Enter your age:")
    get_gender = input("Enter your gender:")

    data = myuser.create_user(get_name, get_id, get_password, get_age, get_gender)
else:
    print("invalid syntax")

#a = collection.find_one()