class product:
    def __init__(self, name, **kwargs):

        super().__init__(**kwargs)
        self.name = name

    def prod(self):
        print("product is", self.name)

# Single Inheritance
class items(product): 
    def item(self):
        print(f"item Name: {self.name}")

it = items(name="soap")
it.item()


class price:
    def __init__(self, amt, **kwargs):
        super().__init__(**kwargs)
        self.amt = amt
    
    def prices(self):
        print(f"price is {self.amt}")

rate = price(amt=50)
rate.prices()


# Multiple Inheritance 
class details(product, price):
    def __init__(self, name, amt):

        super().__init__(name=name, amt=amt)

    def detail(self):
        print(f"the product is {self.name} and its price is {self.amt}")

det = details(name="soap", amt=50)
det.detail()