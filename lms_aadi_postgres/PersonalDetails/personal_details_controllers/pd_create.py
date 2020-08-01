from PersonalDetails.personal_details_modules import create_pd

to_create = create_pd.CreateDetails()
hobbies = ["cricket", "football", "esports"]
details = to_create.create_details("1", "24_07_1998", "B_positive", "BE", hobbies)
print("Details created")
