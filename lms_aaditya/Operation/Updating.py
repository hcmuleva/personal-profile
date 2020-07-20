from ContactsModules.update_contacts import UpdateContact


new_name = input("Enter name to update : ")
new_email = input("Enter Email-Id to update : ")
new_phone = int(input("Enter phone number to update : "))
reg_id = input("Enter registered id to update : ")

update = UpdateContact(new_name, new_email, new_phone, reg_id)
update.update()
print("Contact id : ({}) updated".format(reg_id))
