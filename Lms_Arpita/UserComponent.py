class UserComponent:
    #def __init__():
        # self.user_name = user_name
        # self.user_email = user_email
        # self.user_password = user_password

    def create(self,user_name, user_email, user_password):
        print(f'{user_name} email {user_email} AND PASSWORD {user_password}')

myComponent =UserComponent()
myComponent.create("Harish", "hcmuleva@gmail.com", "Welcome123")