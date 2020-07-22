from PersonalDetails.PdModules import create_pd

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

res = create_pd.PersonalDetails(reg_id, bgroup, academ, fname, mname, hobbies)
res.details()
print("Details registered")
