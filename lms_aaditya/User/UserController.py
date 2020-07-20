from User.UserLogin import User
from ContactsModules.create_contacts import CreateContact
from ContactsModules.read_contacts import ReadContact
from ContactsModules.update_contacts import UpdateContact
from ContactsModules.delete_contact import DeleteContact

print("="*10, "Welcome user", "="*10)
get_in = input("Do you want to register account press y else n ?").lower()

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

else:
    print("Invalid input")

print("*" * 100)

print("user components - \n1) Contacts \n2) Address \n3) Details")
comp_inp = input("Input commands - \n'1' for Contacts \n'2' for Address \n'3' for Details")

if comp_inp == '1':

    print("you want to create, read, update or delete")
    get_cr = input("Input commands ----- \n'C' to create \n'R' to read \n'U' to update \n'D' to delete \n Enter :  ").upper()

    if get_cr == "C":
        my_reg_id = input("Enter your registration id : ")
        my_name = input("Enter your name : ")
        my_email = input("Enter your email : ")
        my_phone = int(input("enter your contact number : "))
        push = CreateContact(my_reg_id, my_name, my_email, my_phone)
        push.create()
        print("Contact created")

    elif get_cr == "R":
        get_id = input("Enter registration id : ")
        a = ReadContact(get_id)
        b = a.read()
        myarr = []
        for i in b:
            myarr.append(i)
        print(myarr)

    elif get_cr == "U":
        new_name = input("Enter name to update : ")
        new_email = input("Enter Email-Id to update : ")
        new_phone = int(input("Enter phone number to update : "))
        reg_id = input("Enter registered id to update : ")
        update = UpdateContact(new_name, new_email, new_phone, reg_id)
        update.update()
        print("Contact id : ({}) updated".format(reg_id))

    elif get_cr == "D":
        get_id = input("Enter registration Id to delete :")
        a = DeleteContact(get_id)
        a.delete()
        print("Contact deleted id {}".format(get_id))

    else:
        print("Invalid input")

else:
    print("Invalid input")
