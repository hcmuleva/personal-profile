from ContactsModules.update_contacts import UpdateContact

new_name = input("Enter name to update : ")
new_email = input("Enter Email-Id to update : ")
new_phone = int(input("Enter phone number to update : "))
doc_id = input("Enter document id to update : ")

update = UpdateContact(new_name, new_email, new_phone, doc_id)
update.update()
print("Contact id : ({}) updated".format(doc_id))
