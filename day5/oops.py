class products:
    def __init__(item,name,price):
        
        item.name = name
        item.price = price

    def bill(item,qty):
            
        total = item.price * qty
        print(f"{item.name} = ",item.price)
        print("quantity = ",qty)
        print("total = ",total)
        return total

p1 = products("soap",50)
p2 = products("oil",40)

grand_total = 0
grand_total += p1.bill(3)
grand_total += p2.bill(1)


print("grand total = ",grand_total)