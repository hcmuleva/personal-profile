from test_module import mongoConnection
p = mongoConnection.path()
collection = p.db["list_item"]

class Shopping:
    def __init__(self,item,qty,price):
        self.item = item
        self.qty = qty
        self.price = price
    def ShoppingList(self):
        mylist={
            "item1": self.item,
            "qty": self.qty,
            "price": self.price

        }
        return collection.insert_one(mylist)

# result = Shopping("chocolate",5,20)
# print(result.ShoppingList());