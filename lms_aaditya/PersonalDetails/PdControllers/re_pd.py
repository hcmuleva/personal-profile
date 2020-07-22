from PersonalDetails.PdModules import read_pd

get_reg_id = input("Enter registration id : ")
a = read_pd.ReadDetails(get_reg_id)
b = a.read_details()
myarr = []
for i in b:
    myarr.append(i)
print(myarr)
