class product:
    def __init__(self,name,*args):
        super().__init__(*args)
        self.name = name

    def prod(self):
        print("product is",self.name)

class items(product): # single inheritance
    def item(self):
        print(self.name)

it = items(name = "ajay")
it.item()

class price:
    def __init__(self,amt,*args):
        super().__init__(*args)
        self.amt = amt
    
    def prices(self):
        print(f"price is {self.amt}")

rate = price(amt = 50)
rate.prices()

class details(product,price):
    def detail(self):
        print(f"the product is {self.name} and its price is {sself.amt}")

det = details(name = "ajay")
det.detail()