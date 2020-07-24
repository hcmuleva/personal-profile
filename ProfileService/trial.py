from flask import Flask, jsonify, request

app = Flask(__name__)

shoppinglist = [{
    "name_snacks": ["chocolates", ",ice cream", "chips"],
    "qty_each": [5, "1L", 2]
},
    {
        "name_veggies": ["potato", "onion", "chillies"],
        "qty_each": ["2Kgs", "4Kgs", "300g"]
    }
]


@app.route('/shoppinglist')
def shopping():
    return jsonify(shoppinglist)

@app.route('/shoppinglist', methods =['POST'])
def add_list():
    item = request.get_json()
    shoppinglist.append(item)
    return {'id': len(shoppinglist)}, 200

@app.route('/shoppinglist/<int:index>', methods = ['PUT'])
def update_list(index):
    item = request.get_json()
    shoppinglist[index] = item
    return  jsonify(shoppinglist[index]), 200

@app.route('/shoppinglist/<int:index>', methods = ['DELETE'])
def delete_list(index):
    shoppinglist.pop(index)
    return 'None', 200


app.run()



