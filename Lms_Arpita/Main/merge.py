from Lms_Arpita.UserBook.UserLogin import User
from Lms_Arpita.Location.addressbook import User_address
from Lms_Arpita.ContactBook.ContactInfo import Contacts
from Lms_Arpita.PersonalDetails.BioData import Bio

myuser = User()
mycontacts = Contacts()
myaddress = User_address()
mybio = Bio()
get_reg = input("Already Registerd? yes/no:")

if get_reg == "yes":
    get_id = input("Enter Email Id:")
    get_password = input("Enter password:")
    get_info = myuser.login(get_id, get_password)
elif get_reg == "no":
    print("Kindly fill the given details")
    get_name = input("Enter user_name:")
    get_id = input("Enter user_id:")
    get_password = input("Enter password:")
    get_age = input("Enter your age:")
    get_gender = input("Enter your gender:")

    data = myuser.create_user(get_name, get_id, get_password, get_age, get_gender)
    print("Registerd Successfully\n")
    print("Please reload page now")
else:
    print("invalid syntax")

get_objid = input("Do you want your unique/object id yes/no:")

get_id = input("Enter Email Id:")
get_password = input("Enter Password:")
myobjecid = myuser.getId(get_id, get_password)
print(myobjecid, "\n")

mycontactid = mycontacts.geContactId(myobjecid)
myaddressid = myaddress.geContactId(myobjecid)


get_api = input("Are you looking for contacts or address or personal detail?\n "
                "for contact type c ,for address type a and for personal details type p:")

if get_api == "c":
    crud = input("do u want to add read update or delete- \n "
                 "for adding new contacts type c"
                 "for getting your contact detail type r"
                 "for updating your contact details type u"
                 "for deleting your contact details type d  ")
    if crud == "c":
        get_object_id = myobjecid
        get_user_name = input(" enter your name:")
        get_phone_no = input(" enter phone_number:")
        mycontacts.create_contact(get_object_id,get_user_name,get_phone_no)
        print("your contact has been successfully created")
    elif crud == "r":
        get_object_id = myobjecid
        mycontacts.get_contact(get_object_id)
    elif crud == "u":
        get_contact_id = mycontactid
        get_updateddata= input("Using these key names update your data {'name': 'your name'},{' phone_number': 'phone no.'}")
        mycontacts.update_contact(get_contact_id,get_updateddata)
        print("your contact has been successfully updated")
    elif crud == "d":
        get_contact_id = mycontactid
        mycontacts.delete_contact(get_contact_id)
        print("your contact has been successfully deleted")
    else:
        print("invalid syntax")
elif get_api == "a":
    crud = input("do u want to add read update or delete- \n "
                 "for adding new address type c"
                 "for getting your address detail type r"
                 "for updating your address details type u"
                 "for deleting your address details type d  ")
    if crud == "c":
        get_object_id = myobjecid
        get_house_no = input(" enter your house no:")
        get_house_name = input("enter your house name:")
        get_street_name = input("enter your street name:")
        get_city_name = input("enter your city name:")
        get_pincode = input("enter your pincode:")
        myaddress.create_address(get_object_id, get_house_no, get_house_name,get_street_name,get_city_name,get_pincode)
        print("your address has been successfully added")
    elif crud == "r":
        get_object_id = myobjecid
        myaddress.get_addresses(get_object_id)
    elif crud == "u":
        get_address_id = myaddressid
        get_updateddata = input("Using these key names update your data"
                           '{"object_id":"your address object_id"}'
                           '{ "house_No": "your new house_no"}'
                           '{ "house_Name": "your new house_name"}'
                           '{"street_Name": "your new street_name"}'
                           '{"city_Name": "you new city_name"}'
                           '{"pincode": "your new pincode"}')
        myaddress.update_address(get_address_id, get_updateddata)
        print("your addess has been successfully updated")
    elif crud == "d":
        get_address_id = myaddressid
        mycontacts.delete_contact(get_address_id)
        print("your address has been successfully deleted")
    else:
        print("invalid syntax")
elif get_api == "p":
    crud = input("do u want to add read update or delete- \n "
                 "for adding new personal type c"
                 "for getting your personal detail type r"
                 )
    if crud == "c":
        get_object_id = myobjecid
        get_parents_name = input("enter you parents name:")
        get_siblings_name = input("enter you siblings name:")
        get_blood_group = input("enter your blood group:")
        get_hobbies = input("enter your hobbies:")
        mybio.create_bio(get_object_id, get_parents_name, get_siblings_name,get_blood_group,get_hobbies)
        print("your personal has been successfully added")
    elif crud == "r":
        get_object_id = myobjecid
        mybio.get_bio(get_object_id)
    else:
        print("invalid syntax")

else:
    print("invalid syntax")






