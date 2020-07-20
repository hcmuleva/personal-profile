from User.UserLogin import User

print("Welcome user")
get_in = input("Do you want to register account press y else n ?")

if get_in == "y":
    get_name = input("Enter your user name : ")
    get_pass = input("Enter your password : ")
    get_age = int(input("Enter your age : "))
    get_gender = input("Enter your gender : ")
    a = User()
    a.register(get_name, get_pass, get_age, get_gender)
    print("User registered please exit and login")

elif get_in == "n":
    print("Please login")
    user_name1 = input("Enter user name : ")
    user_pass1 = input("Enter your password : ")
    get_details = User()
    my_user_data = get_details.user_login(user_name1, user_pass1)
    print(my_user_data)

coll_input = input("What do you want to access")