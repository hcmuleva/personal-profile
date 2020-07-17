from ContactsModules.read_contacts import ReadContact

get_id = input("Enter document id : ")
a = ReadContact(get_id)
b = a.read()
myarr = []
for i in b:
    myarr.append(i)
print(myarr)
