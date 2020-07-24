from flask import Flask, jsonify, request
import json
from Lms_Arpita.UserBook.UserLogin import User

app = Flask(__name__)
myuser = User()

@app.route('/user/create',methods =['POST'])
def Create():
    data = request.get_json()
    req_data = myuser.create_user(data)
    return str(data)
@app.route('/user/read',methods =['POST'])
def Read():
    id_password_req = request. get_json()
    mydata = myuser.login(id_password_req['Email_id'], id_password_req['Password'])
    return str(mydata)
@app.route('/user/update',methods =['Put'])
def Update():
    objid_ndata = request.get_json()
    newdata = myuser.update_user(objid_ndata['_id'], objid_ndata['New_Data'])
    return str(newdata)
@app.route('/user/delete',methods =['DELETE'])
def Delete():
    objid = request.get_json()
    removedata = myuser.delete_user(objid['_id'])
    return str(removedata)

app.run()


# def get_user_page():
#     myuserData= request.get_json()
#     myuser = User()
#
#     user_info = myuser.login(myuserData['userid'], myuserData['password'])
#
#
#     print(user_info, "\n")
#     return str(user_info)
