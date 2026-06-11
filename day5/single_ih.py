class product:
    def __init__(self,name):
        self.name = name

    def prod(self):
        print("product is",self.name)

class items(product):
    def item(self):
        print(self.name)

it = items(name = "ajay")
it.item()