products = ("soap","shmapoo","oil")

item1 = products[0] # index(accessing)
print(item1)

item12 = products[0:2] # slicing
print(item12)

soap = products.count("soap") # count()
print(soap)

isoil = products.index("oil") # index()
print(isoil)

length = len(products) # length
print(length)

issoap = "soap" in products # membership opt
print(issoap)

# Nested tuple
products = (("soap",50),("shampoo",90),("oil",40))
item1 = products[0][1]
print(item1)