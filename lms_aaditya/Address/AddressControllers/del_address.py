from Address.AddressModules.delete_address import DeleteAddress

get_id = input("Enter registration Id to delete :")
a = DeleteAddress(get_id)
a.delete_add()
print("Address deleted id {}".format(get_id))
