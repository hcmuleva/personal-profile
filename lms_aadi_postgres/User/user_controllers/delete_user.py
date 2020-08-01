from User.user_modules import user_delete

delete = user_delete.UserDelete()
to_delete = delete.user_delete("3")
print("Deleted successfully")
