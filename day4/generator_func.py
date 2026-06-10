def products():
    products = []
    while True:
        product = input("enter the products :")
        price = input("enter the price :")
        products.append([product,price])

        more = input("need more products yes/no :")
        if(more == "no"):
            break          
    yield products

gen = products()
for item in gen:
    print(item)