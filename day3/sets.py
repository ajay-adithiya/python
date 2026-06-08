products = set()
price = set()
while True:
    items = input("enter the products :")
    products.add(items)

    more = input("need another item ? yes/no :")
    if(more == "no"):
        break
print("products are :",products)

products.update(["face wash","brush"]) # update(
print(products)

products.remove("soap") # remove()
print(products)

products.discard("soap") # discard()
print(products)

check = "soap" in products # membership opt
print(check)


while True:
    prices = input("enter price of products : ")
    more = input("any other item ? yes/no :")
    if(more == "no"):
        break
print(price.add(prices))
prod_price = products.union(price) # union()
print(prod_price)

for item in products: # iteration
    cust1 = input("enter cust1 products :")
    more = input("need another item ? yes/no :")
    if(more == "no"):
        break
    
    cust2 = input("enter cust2 products :")
    more = (input("need another item ? yes/no :"))
    if(more == "no"):
        break

print(cust1)
print(cust2)

# items = cust1.union(cust2) # union()
# print(items)

# common = cust1.intersection(cust2) # intersection()
# print(common)

