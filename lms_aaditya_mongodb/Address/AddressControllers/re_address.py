from Address.AddressModules import read_address

get_add_id = input("Enter registration id : ")
a = read_address.ReadAddress(get_add_id)
b = a.read_add()
myarr = []
for i in b:
    myarr.append(i)
print(myarr)
