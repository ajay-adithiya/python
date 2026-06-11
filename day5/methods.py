# instance (self)
class products:
    def __init__(self,item,price):
        self.item = "soap"
        self.price = 50

    def bill(self,qty):
        total = 0
        amt = self.price * qty
        total += amt
        print(total)

bill1 = products(item = "soap",price = 50)
bill1.bill(3)

# class (cls)
class product:
    item = "soap"
    price = 50

    @classmethod
    def change_item(cls):
        cls.item = "shampoo"
        print(f"item is {cls.item}")
    @classmethod
    def change_price(cls):
        cls.price = 90
        print("price is 90")

    @staticmethod
    def item_change():
        item = "oil"
        print(item)

change = product()
product.change_item()
product.change_price()

product.item_change()

