# error that occurs while program runs
products = []
quantity = []
price = []
while True:
    product = input("enter available products :")
    qty = input("enter products quantity :")
    prices = input("enter products price :")
    products.append(product)
    quantity.append(qty)
    price.append(prices)

    more = input("need another item ? yes/no :")
    if(more == "no"):
        break

try :
    total = 0
    for i,j in zip(quantity,price):
        amt = float(i) * float(j)
        total += amt
    print("total amount : ",total)

except :
    print("no items found")

else :
    print("thanks for shopping")