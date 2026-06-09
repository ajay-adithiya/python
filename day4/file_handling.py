# opening file
file = open("products.txt","w") # write
file.write("soap\n")
file.write("shampoo\n")
file.write("oil\n")
file.close()

file = open("products.txt","r") # read
items = file.read()
print(items)
file.close()

file = open("products.txt","r") # readline
item1 = file.readline()
item2 = file.readline()
print(item1)
print(item2)
file.close()

file = open("products.txt","r") # read lines
items = file.readlines()
print(items)
file.close()

file = open("products.txt","a") # append
file.write("facewash\n")
file.close()

with open("products.txt","r") as file:
          items = file.read()    # with statement
          print(items)

products = []
price = []
while True:
        product = input("enter products :")
        prices = input("enter price :")

        products.append(product)
        price.append(prices)

        more = input("need another item ? yes/no :")
        if(more == "no"):
            break

bill = open("bill.txt","w")
bill.write("prodcuts : price\n")
for i, j in zip(products, price):
        bill.write(f"{i} : {j}\n")
bill.close()

bill = open("bill.txt","r")
final = bill.read()
print(final)
bill.close()
