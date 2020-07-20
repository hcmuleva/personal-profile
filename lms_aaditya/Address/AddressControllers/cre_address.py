from Address.AddressModules import create_address

my_reg_id = input("Enter your registration id : ")
my_house_num = int(input("Enter house number : "))
my_street = input("Enter street or lane : ")
my_city = input("Enter city : ")
my_district = input("Enter district : ")
my_state = input("Enter state : ")
my_pincode = int(input("Enter your pincode : "))

push = create_address.CreateAddress(my_reg_id, my_house_num, my_street, my_city, my_district, my_state, my_pincode)
push.create_add()
print("Address created")
