class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def prod(self):
        print(".")
        print(self.name)
        print(self.price)

class soap(product):
    pass

class shampoo(product):
    pass

# child constructor
class oil(product):
    def __init__(self,name,price,discount):
        self.name = name
        self.price = price
        self.discount = discount

    def discount():
        print("discount yeahh")

item = soap(name = "soap",price = 50)
item.prod()
nxt_item = oil(name = "oil",price = 60,discount = 10)
print(nxt_item.name)
print(nxt_item.price)
print("discount in % : ",nxt_item.discount)

# super() - call parent method or constructor
class Soap(product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def Lux(self):
        print(f"{self.name} soap costs {self.price} rupees")

soap = Soap(name = "lux",price = 35)
soap.Lux()

# method overriding
class overriding(product):
    def prod(self):
        print("null")

over = overriding(name = "soap",price = 50)
over.prod()

