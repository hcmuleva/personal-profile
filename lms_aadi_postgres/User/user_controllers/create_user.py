from User.user_modules import user_create

my_user_create = user_create.CreateUser()
to_read = my_user_create.create_user("aaditya muleva", "aaditya_new_123", 23, "male")
print(to_read)
