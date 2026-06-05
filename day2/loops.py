# items
item = ["soap","shampoo","oil"]
item_count = [50, 75, 80]
item_cost = [50, 90, 40]

total_products = 0

L = len(item)

# for loop
for i in range(L):
    print(item[i],"=",item_count[i])
    total_products += item_count[i]

print("total products in store :",total_products)

# while loop
total = 0

while True:
    product = input("enter product :")
    if(product == "soap"):
        total += 50
    elif(product == "shampoo"):
        total += 90
    elif(product == "oil"):
        total += 40
    else:
        print("product unavailable")

    more = input("Adding more prodcuts : yes/no ")
    if(more == "no"):
        break

print("total bill = ",total)

# for loop in list
for product in item :
    print(product)

# for loop in string
item1 = "soap"
item2 = "shampoo"
item3 = "oil"

for letters in item1:
    print(letters)