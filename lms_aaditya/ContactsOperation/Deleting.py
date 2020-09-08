from ContactsModules.delete_contact import DeleteContact

get_id = input("Enter registration Id to delete :")

a = DeleteContact(get_id)
a.delete()
print("Contact deleted id {}".format(get_id))
