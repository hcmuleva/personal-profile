from Lms_Arpita.MongoDb.UserFile import Detail
userapi = Detail()
#userapi.user()
myUserData=userapi.autheticateUser("hcm@gmail.com", "welcome1")
print(myUserData)
for i in range (20,30):
    myCreatedUser=userapi.createUser("krishna"+str(i),"k1@gmail.com"+str(i),"welcome",13,"Bangalore")
    print(myCreatedUser)

