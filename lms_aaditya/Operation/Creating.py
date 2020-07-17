from ContactsModules.create_contacts import CreateContact

my_name = input("Enter your name : ")
my_email = input("Enter your email : ")
my_phone = int(input("enter your contact number : "))

push = CreateContact(my_name, my_email, my_phone)
push.create()
print("Contact created")
