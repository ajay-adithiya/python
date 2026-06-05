items = ""
products = []

while True:
    
    items = input("enter the items :")
    items = items.capitalize().strip()
    products.append(items)
    
    more = input("need another item ? yes/no :").strip().lower() # string methods

    if(more == "no"):
        break

print(f"items are :{products} ") # string formatting

# string slicing
item1 = products[0][1:4]
print(item1)

# string concatenation
if(len(products) == 1):
    print(products)
else :
    concat = products[0] + "," + products[1]
    print(concat)

# string repetation
if(len(products) >= 3):
    rpt = products[2]*3
    print(rpt)

# find()
item1 = products[0]
L = item1.find("o")
print(L)

# count()
C = item1.count("p")
print(C)

# replace()
replaced = item1.replace(products[0],"pen")
print(replaced)