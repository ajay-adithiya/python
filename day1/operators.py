# items
item1 = "soap"
item2 = "shampoo"
item3 = "oil"

item_count = {item1 : 50 , item2 : 75 , item3 : 80}

# items price
item1_price = float(input("enter item1 price :"))
item2_price = float(input("enter item2 price :"))
item3_price = float(input("enter item3 price :"))

# no. of items sold
item1_sold = int(input("enter no. of item1 sold :"))
item2_sold = int(input("enter no. of item2 sold :"))
item3_sold = int(input("enter no. of item3 sold :"))

# profit
profit1 = item1_price * item1_sold
profit2 = item2_price * item2_sold
profit3 = item3_price * item3_sold

print("profit by item1 = ",profit1)
print("profit by item2 = ",profit2)
print("profit by item3 = ",profit3)

# total profit
total_profit = profit1 + profit2 + profit3
print("tot profit per day =",total_profit)

# avg sales per day
avg_sales = (item1_sold + item2_sold + item3_sold)/3
print("avg sales per day =",avg_sales)

# comparison operators
if(profit1 >= profit2):
    print("profit1 gave more income")

# logical operators 
if(profit1 and profit2 and profit3 > 200):
    print("sales good")

price_list = [item1_price, item2_price, item3_price]
item_count != price_list

# membership operator
print(item1_price in price_list)    

# idendity operator
print(item_count is price_list)