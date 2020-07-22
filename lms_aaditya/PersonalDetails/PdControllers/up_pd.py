from PersonalDetails.PdModules import update_pd

reg_id = input("Enter registered Id : ")
bgroup = input("Enter your blood group : ")
academ = input("Enter your last or current academic detail : ")
fname = input("Enter your fathers name : ")
mname = input("Enter your mothers name : ")

temp = 'y'
hobbies = []
while temp == 'y':
    hb = input("Enter your hobbies : ").lower()
    hobbies.append(hb)
    get_inp = input("You want to enter more? y/n : ")
    if get_inp == 'y':
        temp = 'y'
    else:
        temp = 'n'

res = update_pd.UpdateDetails(reg_id, bgroup, academ, fname, mname, hobbies)
res.update_details()
print("Details updated")
