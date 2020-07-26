from User.UserLogin import User
from ContactsModules.create_contacts import CreateContact
from ContactsModules.read_contacts import ReadContact
from ContactsModules.update_contacts import UpdateContact
from ContactsModules.delete_contact import DeleteContact
from Address.AddressModules import create_address
from Address.AddressModules import read_address
from Address.AddressModules import update_address
from Address.AddressModules.delete_address import DeleteAddress
from PersonalDetails.PdModules import create_pd
from PersonalDetails.PdModules import read_pd
from PersonalDetails.PdModules import update_pd
from PersonalDetails.PdModules import delete_pd
from flask import Flask, request

app = Flask(__name__)

my_user = User()
my_create_contact = CreateContact()
my_read_contact = ReadContact()
my_update_contact = UpdateContact()
my_del_contact = DeleteContact()
my_create_address = create_address.CreateAddress()
my_read_address = read_address.ReadAddress()
my_update_address = update_address.UpdateAddress()
my_del_address = DeleteAddress()
my_create_details = create_pd.PersonalDetails()
my_read_pd = read_pd.ReadDetails()
my_update_pd = update_pd.UpdateDetails()
my_del_pd = delete_pd.DeleteDetails()


@app.route("/user/register", methods=["POST"])
def user_register():
    data = request.get_json()
    created_data = my_user.register(data)
    return str(created_data)


@app.route("/user/login", methods=["POST"])
def user_login():
    user_data = request.get_json()
    login_details = my_user.user_login(user_data)
    return str(login_details)


@app.route("/user/contacts/create", methods=["POST"])
def create_contact():
    create_contact_data = request.get_json()
    contact_details = my_create_contact.create(create_contact_data)
    return str(create_contact_data)


@app.route("/user/contacts/read", methods=["POST"])
def read_contact():
    read_contact_data = request.get_json()
    contact_data = my_read_contact.read(read_contact_data)
    myarr = []
    for i in contact_data:
        myarr.append(i)
    print(myarr)
    return str(contact_data)


@app.route("/user/contacts/update", methods=["PUT"])
def update_contact():
    update_contact_data = request.get_json()
    updated_data = my_update_contact.update(update_contact_data["Registration Id"], update_contact_data["new_data"])
    return str(updated_data)


@app.route("/user/contacts/delete", methods=["DELETE"])
def delete_contact():
    delete_contact_id = request.get_json()
    del_id = my_del_contact.delete(delete_contact_id)
    return str(del_id)


@app.route("/user/address/create", methods=["POST"])
def create_address():
    create_address_data = request.get_json()
    contact_details = my_create_address.create_add(create_address_data)
    return str(create_address_data)


@app.route("/user/address/read", methods=["POST"])
def read_address():
    read_add_data = request.get_json()
    read_add = my_read_address.read_add(read_add_data)
    myarr = []
    for i in read_add:
        myarr.append(i)
    print(myarr)
    return str(read_add)


@app.route("/user/address/update", methods=["PUT"])
def update_address():
    update_address_data = request.get_json()
    update_add = my_update_address.update_add(update_address_data["Registration Id"], update_address_data["new_data"])
    return str(update_add)


@app.route("/user/address/delete", methods=["DELETE"])
def delete_address():
    delete_id = request.get_json()
    del_add = my_del_address.delete_add(delete_id)
    return str(del_add)


@app.route("/user/details/create", methods=["POST"])
def create_details():
    create_details_data = request.get_json()
    my_create_details.details(create_details_data)
    return str(create_details_data)


@app.route("/user/details/read", methods=["POST"])
def read_details():
    read_details_data = request.get_json()
    ret_data = my_read_pd.read_details(read_details_data)
    myarr = []
    for i in ret_data:
        myarr.append(i)
    print(myarr)
    return str(ret_data)


@app.route("/user/details/update", methods=["PUT"])
def update_details():
    update_details_data = request.get_json()
    up_details = my_update_pd.update_details(update_details_data["Registration Id"], update_details_data["new_data"])
    return str(up_details)


@app.route("/user/details/delete", methods=["DELETE"])
def delete_details():
    del_id = request.get_json()
    del_details = my_del_pd.delete_details(del_id)
    return str(del_details)


if __name__ == "__main__":
    app.run()
