products = ["soap","shampoo","oil"]
prices = [50,90,40]

new_price = [price * 1.18 for price in prices]
print(new_price)

# string manipulation
upper = [item.upper() for item in products]
print(upper)

# string filtering 
bigstr = [item for item in products if len(item) > 3]
print(bigstr)

# if - else
cost = ["costly" if price <= 70 else "costly" for price in prices]
print(cost)

# nested - for
pairs = [(i,j) for i in range(3) for j in range(3)]
print(pairs)