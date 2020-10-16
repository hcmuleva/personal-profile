from flask import Flask, request
from Create.create_keys import CreateKeyValue
from Read.read_keys import GetValues
from Updates.update_data import RenameKeys
from MoveData.swap_database import SwapDatabase
from Checking.check_db import CheckDatabase
from Delete.del_key import DelKeys
from Delete.flush_db import FlushDB
from Delete.flushall import FlushAllDb


app = Flask(__name__)


@app.route("/create_single_key_value", methods=["POST"])
def create_single_key():
    my_obj = CreateKeyValue()
    data = request.get_json()
    operation = my_obj.single_key_value(data[0], data[1])
    return str(operation)


@app.route("/create_multi_key_value", methods=["POST"])
def create_multi_key_val():
    my_obj = CreateKeyValue()
    json_data = request.get_json()
    operation = my_obj.multiple_key_value(json_data)
    return str(operation)


@app.route("/get_single_key_value", methods=["GET"])
def get_single_value():
    my_obj = GetValues()
    my_key = request.get_json()
    operation = my_obj.get_single_value(my_key)
    return str(operation)


@app.route("/get_multi_key_value", methods=["GET"])
def get_multi_key_value():
    my_obj = GetValues()
    my_keys = request.get_json()
    my_val_list = []
    for i in range(len(my_keys)):
        my_val_list.append(my_obj.get_multiple_values(my_keys[i]))
    final = zip(my_keys, my_val_list)
    my_final_list = []
    for j in final:
        my_final_list.append(j)
    return str(my_final_list)


@app.route("/get_all_keys", methods=["GET"])
def get_all_keys():
    my_obj = GetValues()
    opr = my_obj.get_all_keys()
    return str(opr)


@app.route("/get_random_key", methods=["GET"])
def get_random_key():
    my_obj = GetValues()
    opr = my_obj.get_random_key()
    return str(opr)


@app.route("/rename_keys", methods=["PUT"])
def update_key_name():
    my_obj = RenameKeys()
    data = request.get_json()
    operation = my_obj.rename_key(data[0], data[1])
    return str(operation)


@app.route("/move_key_to_another_db", methods=["PUT"])
def move_key_to_another_db():
    my_obj = RenameKeys()
    data = request.get_json()
    operation = my_obj.move_key_to_another_db(data[0], data[1])
    return str(operation)


@app.route("/swap_all_data_from_one_db_to_another", methods=["PUT"])
def swap_all_data_from_one_db_to_another():
    my_obj = SwapDatabase()
    database_no = request.get_json()
    operation = my_obj.move_data(database_no[0], database_no[1])
    return str(operation)


@app.route("/check_key_type", methods=['GET'])
def check_key_type():
    my_obj = CheckDatabase()
    my_key = request.get_json()
    res = my_obj.check_key_type(my_key)
    return str(res)


@app.route("/check_if_key_exists", methods=['GET'])
def check_key_existance():
    my_obj = CheckDatabase()
    my_key = request.get_json()
    res = my_obj.check_key_exist(my_key)
    return str(res)


@app.route("/delete_keys", methods=['DELETE'])
def delete_keys():
    my_obj = DelKeys()
    keys = request.get_json()
    key_data = []
    for i in keys:
        key_data.append(my_obj.delete_keys(i))
    return str(key_data)


@app.route("/flush_current_db", methods=['DELETE'])
def flush_db():
    my_obj = FlushDB()
    return str(my_obj.clear_all())


@app.route("/clear_all_databases", methods=['DELETE'])
def flush_all():
    my_obj = FlushAllDb()
    return str(my_obj.flush_all_data())


if __name__ == "__main__":
    app.run()
