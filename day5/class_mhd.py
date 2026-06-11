# alter constructor
class product :
    def __init__(self,item,price):
        self.item = item
        self.price = price

    @classmethod
    def prod(cls,data):
        item, price = data.split(",")
        return cls(item,price)
    
bill = product.prod("soap , 50")
print(f"{bill.item} - {bill.price}")

