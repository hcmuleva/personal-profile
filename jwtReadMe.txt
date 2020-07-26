>client enters login details
->info goes to server matches the details from db
-> shows if AUTHENTICATED or not
-> next sm operations can be done only admin(assuming delete operation)
->now that client wants to perform delete operation the server will check if person is authorised or not
->then returns if authorised or not n then we can perform task


so now lets see what shld we code like

///Server///

our login page

@app.route('/user/login',methods =['POST'])
def login():
    id_password_req = request. get_json()
    mydata = myuser.login(id_password_req['Email_id'], id_password_req['Password'])
    return str(mydata)

now we need to get jwt token for each role

 so we can say it like this

 *//import jwt//*
def get_jwt_token (self, Role):
	secret_key = "    "
	token = jwt.encode({"Role":"Role"}, secret_key, algorithm = ['HS256'])
	return str(token)

def return_token(self,token,secret_key):
	decode_val = jwt.decode(token, secret_key, algorithm = ['HS256'])
	return "decode_val"

def check_authorised(self, decode_value)
# say we authorised admin
authorised ="Admin"
if authorised == decode_value:
	print("Authorised\n Enter your operation")
	#say delete
	user.delete("_id":Object_id("id"))
	return "your operation is done"
else:
	return "Unauthorised"

