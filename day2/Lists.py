products = []
while True:
    items = input("enter the products :")
    products.append(items)

    more = input("need another item ? yes/no :")
    if(more == "no"):
        break
print("products are :",products)

item1 = products[-1] # indexing
print("1st item is :",item1)

item12 = products[0 : 2] # slicing
print("1st two items are :",item12)

products[1] = "HairOil" # mutable list
print(products)

added = products.append("face wash") # append()
print(added)

inserted = products.insert(0,"pen") # insert()
print(inserted)

extended = products.extend(["paste","brush"]) #extend()
print(extended)

products.pop() # pop()
print(products)

products.remove("soap") # remove()
print(products)

products.clear() # clear
print(products)

length = len(products) # len()
print(length)

issoap = "soap" in products # checking existence
print(issoap)

oil = products.count("oil") # count()
print(oil)

# nested list
products.clear()
while True:
    P_name = input("enter product :")
    P_amt = float(input("enter product amt :"))

    more = input("need another item ? yes/no :")
    if(more == "no"):
        break

    products.append([P_name,P_amt])
print(products)
