products  = {}
while True:
    items = input("enter the products :")
    price = input("enter the price of product :")
    products[items] = price

    more = input("need another item ? yes/no :")
    if(more == "no"):
        break
print("products are :",products)

get_price = input("enter product : ")
get_price = products.get(get_price) # get()
print(get_price)

products["face wash"] = 150 # update()
print(products)

poped = products.pop(input("enter item to be deleted :")) # pop()
print(poped)
print(products)

# print all keys
keys = products.keys()
print(keys)

# print all values
values = products.values()
print(values)

# print all keys and values
items = products.items()
print(items)

# for loop
for key in products:
    print(key)
    
for value in products.values():
    print(value)

for key,value in products.items():
    print(key," : ",value)

# nested dictionary
nested_products = {}

for item, price in products.items():
    item_no = input(f"Enter item number for {item}: ")

    nested_products[item_no] = {
        "product": item,
        "price": price
    }

print(nested_products)

products.clear() # clear()
print(products)