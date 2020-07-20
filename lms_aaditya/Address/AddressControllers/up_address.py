from Address.AddressModules import update_address


my_up_reg_id = input("Enter your registration id : ")
my_up_house_num = int(input("Enter house number : "))
my_up_street = input("Enter street or lane : ")
my_up_city = input("Enter city : ")
my_up_district = input("Enter district : ")
my_up_state = input("Enter state : ")
my_up_pincode = int(input("Enter your pincode : "))

update = update_address.UpdateAddress(
    my_up_reg_id, my_up_house_num, my_up_street, my_up_city, my_up_district, my_up_state, my_up_pincode)
update.update_add()
print("Address id : ({}) updated".format(my_up_reg_id))
