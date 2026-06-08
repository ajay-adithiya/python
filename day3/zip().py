products = []
price = (50,90,40)
while True:
    items = input("enter the products :")
    products.append(items)

    more = input("need more items ? yes/no :")
    if(more == "no"):
        break
    
print("products are :",products)
print("prices are :",price)

zipped = zip(products,price)
print(list(zipped))

for index,(product,price) in enumerate (zip(products,price)):
    print(index, product, price)