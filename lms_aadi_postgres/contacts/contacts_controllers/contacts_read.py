from contacts.contacts_modules import read_contact

to_read = read_contact.ReadContact()
rows = to_read.read_contact()
for row in rows:
    print("name = ", row[0])
    print("email = ", row[1])
    print("contact number = ", row[2])
