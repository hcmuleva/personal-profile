from User.UserLogin import User
from ContactsModules.create_contacts import CreateContact
from ContactsModules.read_contacts import ReadContact
from ContactsModules.update_contacts import UpdateContact
from ContactsModules.delete_contact import DeleteContact
from Address.AddressModules import create_address
from Address.AddressModules import read_address
from Address.AddressModules import update_address
from Address.AddressModules.delete_address import DeleteAddress
from PersonalDetails.PdModules import create_pd
from PersonalDetails.PdModules import read_pd
from PersonalDetails.PdModules import update_pd
from PersonalDetails.PdModules import delete_pd


def register_user():
    print()
    print("-" * 100)
    print()
    get_name = input("Enter your user name : ")
    get_pass = input("Enter your password : ")
    get_age = int(input("Enter your age : "))
    get_gender = input("Enter your gender : ")
    a = User()
    a.register(get_name, get_pass, get_age, get_gender)
    print("User registered please exit and login")


def user_login():
    print()
    print("-" * 100)
    print()
    print("Please login")
    user_name1 = input("Enter user name : ")
    user_pass1 = input("Enter your password : ")
    get_details = User()
    my_user_data = get_details.user_login(user_name1, user_pass1)
    print(my_user_data)
    if None == my_user_data:
        raise Exception("Sorry, not authenticated")


print("=" * 10, "Welcome user", "=" * 10)
get_in = input("Do you want to register account press y else n ?").lower()

if get_in == "y":
    register_user()

elif get_in == "n":
    user_login()

else:
    print("Invalid input")
print()
print("*" * 100)


def create_contact_comp():
    print()
    print("-" * 100)
    print()
    my_reg_id = input("Enter your registration id : ")
    my_name = input("Enter your name : ")
    my_email = input("Enter your email : ")
    my_phone = int(input("enter your contact number : "))
    push = CreateContact(my_reg_id, my_name, my_email, my_phone)
    push.create()
    print("Contact created")


def read_contact_comp():
    print()
    print("-" * 100)
    print()
    get_id = input("Enter registration id : ")
    a = ReadContact(get_id)
    b = a.read()
    myarr = []
    for i in b:
        myarr.append(i)
    print(myarr)


def update_contact_comp():
    print()
    print("-" * 100)
    print()
    reg_id = input("Enter registered id : ")
    new_name = input("Enter name to update : ")
    new_email = input("Enter Email-Id to update : ")
    new_phone = int(input("Enter phone number to update : "))
    update = UpdateContact(reg_id, new_name, new_email, new_phone)
    update.update()
    print("Contact id : ({}) updated".format(reg_id))


def delete_contact_comp():
    print()
    print("-" * 100)
    print()
    get_id = input("Enter registration Id to delete :")
    a = DeleteContact(get_id)
    a.delete()
    print("Contact deleted id {}".format(get_id))


def create_address_comp():
    print()
    print("-" * 100)
    print()
    my_reg_id = input("Enter your registration id : ")
    my_house_num = int(input("Enter house number : "))
    my_street = input("Enter street or lane : ")
    my_city = input("Enter city : ")
    my_district = input("Enter district : ")
    my_state = input("Enter state : ")
    my_pincode = int(input("Enter your pincode : "))
    push = create_address.CreateAddress(my_reg_id, my_house_num, my_street, my_city, my_district, my_state, my_pincode)
    push.create_add()
    print("Address created")


def read_address_comp():
    print()
    print("-" * 100)
    print()
    get_add_id = input("Enter registration id : ")
    a = read_address.ReadAddress(get_add_id)
    b = a.read_add()
    myarr = []
    for i in b:
        myarr.append(i)
    print(myarr)


def update_address_comp():
    print()
    print("-" * 100)
    print()
    my_up_reg_id = input("Enter your registration id : ")
    my_up_house_num = int(input("Enter house number : "))
    my_up_street = input("Enter street or lane : ")
    my_up_city = input("Enter city : ")
    my_up_district = input("Enter district : ")
    my_up_state = input("Enter state : ")
    my_up_pincode = int(input("Enter your pincode : "))
    update = update_address.UpdateAddress(
        my_up_reg_id, my_up_house_num, my_up_street, my_up_city, my_up_district, my_up_state, my_up_pincode)
    update.update_add()
    print("Address id : ({}) updated".format(my_up_reg_id))


def delete_address_comp():
    print()
    print("-" * 100)
    print()
    get_id = input("Enter registration Id to delete :")
    a = DeleteAddress(get_id)
    a.delete_add()
    print("Address deleted id {}".format(get_id))


def create_details_comp():
    reg_id = input("Enter registered Id : ")
    bgroup = input("Enter your blood group : ")
    academ = input("Enter your last or current academic detail : ")
    fname = input("Enter your fathers name : ")
    mname = input("Enter your mothers name : ")

    temp = 'y'
    hobbies = []
    while temp == 'y':
        hb = input("Enter your hobbies : ").lower()
        hobbies.append(hb)
        get_inp = input("You want to enter more? y/n : ")
        if get_inp == 'y':
            temp = 'y'
        else:
            temp = 'n'

    res = create_pd.PersonalDetails(reg_id, bgroup, academ, fname, mname, hobbies)
    res.details()
    print("Details registered")


def read_detail_comp():
    get_reg_id = input("Enter registration id : ")
    a = read_pd.ReadDetails(get_reg_id)
    b = a.read_details()
    myarr = []
    for i in b:
        myarr.append(i)
    print(myarr)


def update_detail_comp():
    reg_id = input("Enter registered Id : ")
    bgroup = input("Enter your blood group : ")
    academ = input("Enter your last or current academic detail : ")
    fname = input("Enter your fathers name : ")
    mname = input("Enter your mothers name : ")

    temp = 'y'
    hobbies = []
    while temp == 'y':
        hb = input("Enter your hobbies : ").lower()
        hobbies.append(hb)
        get_inp = input("You want to enter more? y/n : ")
        if get_inp == 'y':
            temp = 'y'
        else:
            temp = 'n'

    res = update_pd.UpdateDetails(reg_id, bgroup, academ, fname, mname, hobbies)
    res.update_details()
    print("Details updated")


def delete_detail_comp():
    get_reg_id = input("Input registration Id : ")

    a = delete_pd.DeleteDetails(get_reg_id)
    a.delete_details()
    print("Details deleted ")


print("user components - \n1) Contacts \n2) Address \n3) Details")
print()
comp_inp = input("Input commands - \n'1' for Contacts \n'2' for Address \n'3' for Details \nEnter : ")

if comp_inp == '1':
    print()
    print("=" * 100)
    print()
    print("You want to create, read, update or delete")
    get_contact_input = input(
        "Input commands ----- \n'C' to create \n'R' to read \n'U' to update \n'D' to delete \nEnter :  ").upper()

    if get_contact_input == "C":
        create_contact_comp()

    elif get_contact_input == "R":
        read_contact_comp()

    elif get_contact_input == "U":
        update_contact_comp()

    elif get_contact_input == "D":
        delete_contact_comp()

    else:
        print("Invalid input")

elif comp_inp == '2':
    print()
    print("=" * 100)
    print()
    print("You want to create, read, update or delete")
    get_address_input = input(
        "Input commands ----- \n'C' to create \n'R' to read \n'U' to update \n'D' to delete \nEnter :  ").upper()
    if get_address_input == "C":
        create_address_comp()

    if get_address_input == 'R':
        read_address_comp()

    if get_address_input == 'U':
        update_address_comp()

    if get_address_input == "D":
        delete_address_comp()

elif comp_inp == '3':
    print()
    print("=" * 100)
    print()
    print("You want to create, read, update or delete")
    get_details_input = input(
        "Input commands ----- \n'C' to create \n'R' to read \n'U' to update \n'D' to delete \nEnter :  ").upper()
    if get_details_input == "C":
        create_details_comp()

    elif get_details_input == "R":
        read_detail_comp()

    elif get_details_input == "U":
        update_detail_comp()

    elif get_details_input == "D":
        delete_detail_comp()

else:
    print("Invalid input")
