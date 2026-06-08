# def products(*args): --> stores values in tuples
# def prosucts(** args): --> stored values in dictionary 
products = []
price = []
while True:
    product = input("enter available products :")
    prices = input("enter products price :")
    products.append(product)
    price.append(prices)

    more = input("need another item ? yes/no :")
    if(more == "no"):
        break
    
print("products are :",products)
print("prices are :",price)

cust1 = []
cost = []
while True:
    items = input("enter the product chosen :")
    cust1.append(items)
    costs = input("enter the price of product :")
    cost.append(costs)
    more = input("need another item ? yes/no :")
    if(more == "no"):
        break

# def function
def bill(*args):
    total = 0
    for amt in cost:
        total += float(amt)

    print("Total bill amount is :",total)
    return total

total = bill(cost)

def store(**kwargs):
    purchased_dict = dict(zip(cust1,cost))
    print("purchase = ",purchased_dict)

store(cust1 = cust1, cost = cost)

discount = lambda x : x * 0.18
print("discount price = ",discount(float(total)))