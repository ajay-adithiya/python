item = ["soap","shampoo","oil"]


total = 0

while True:
    product = input("enter product :")
    match product :
        case "soap" :
            price = 50
        case "shampoo":
            price = 90
        case "oil" :
            price = 40
        case _:
            print("product not avaialable")

    more = input("need another proudcut? yes/no :")

    total += price
    if (more == "no"):
        break        
print("total = ",total)