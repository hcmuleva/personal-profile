from ContactsModules.update_contacts import UpdateContact


reg_id = input("Enter registered id to update : ")
new_name = input("Enter name to update : ")
new_email = input("Enter Email-Id to update : ")
new_phone = int(input("Enter phone number to update : "))


update = UpdateContact(reg_id, new_name, new_email, new_phone)
update.update()
print("Contact id : ({}) updated".format(reg_id))
