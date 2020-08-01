from PersonalDetails.personal_details_modules import read_pd

to_read = read_pd.ReadDetails()
rows = to_read.read_details()
print("Details --")
for row in rows:
    print("user id = ", row[0])
    print("birth date = ", row[1])
    print("blood group = ", row[2])
    print("academic details = ", row[3])
    print("hobbies = ", row[4])
