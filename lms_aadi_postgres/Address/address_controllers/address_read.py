from Address.address_modules import read_address

to_read = read_address.ReadAddress()
rows = to_read.read_address()
for row in rows:
    print("User_id = ", row[0])
    print("house_number = ", row[1])
    print("street = ", row[2])
    print("city = ", row[3])
    print("city = ", row[4])
    print("district = ", row[5])
    print("state = ", row[6])
