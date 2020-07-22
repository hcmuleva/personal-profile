from PersonalDetails.PdModules import delete_pd

get_reg_id = input("Input registration Id : ")

a = delete_pd.DeleteDetails(get_reg_id)
a.delete_details()
print("Details deleted ")
