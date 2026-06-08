products = set()
price = set()

# Product input
while True:
    item = input("Enter product : ")
    products.add(item)

    more = input("Need another item ? yes/no : ")
    if more == "no":
        break

print("Products :", products)

# Update
products.update(["face wash", "brush"])
print(products)

# Remove
products.discard("soap")
print(products)

# Membership
print("soap" in products)

# Price input
while True:
    p = input("Enter price : ")
    price.add(p)

    more = input("Any other price ? yes/no : ")
    if more == "no":
        break

print("Prices :", price)

# Union
prod_price = products.union(price)
print("Union :", prod_price)

# Customer 1
cust1 = set()

while True:
    item = input("Enter Customer 1 product : ")
    cust1.add(item)

    more = input("Need another item ? yes/no : ")
    if more == "no":
        break

# Customer 2
cust2 = set()

while True:
    item = input("Enter Customer 2 product : ")
    cust2.add(item)

    more = input("Need another item ? yes/no : ")
    if more == "no":
        break

print("Customer 1 :", cust1)
print("Customer 2 :", cust2)

# Union
all_products = cust1.union(cust2)
print("All Products :", all_products)

# Intersection
common_products = cust1.intersection(cust2)
print("Common Products :", common_products)

# Difference
print("Only Customer 1 :", cust1 - cust2)
print("Only Customer 2 :", cust2 - cust1)