from User.user_modules import user_read

res = user_read.UserRead()
rows = res.user_read()
for row in rows:
    print("user_id = ", row[0])
    print("user_name = ", row[1])
    print("user_password = ", row[2])
    print("age = ", row[3])
    print("gender = ", row[4])
