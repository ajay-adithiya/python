mobile_unbox = set({"phone","case","adapter","cable"})
laptop_unbox = set({"laptop","adapter","cable"})

# union()
electronic_gadgets = mobile_unbox.union(laptop_unbox)
print(electronic_gadgets)

# intersection()
common_items = mobile_unbox.intersection(laptop_unbox)
print(common_items)

# difference()
only_mobile = mobile_unbox.difference(laptop_unbox)
print(only_mobile)
only_laptop = laptop_unbox - mobile_unbox
print(only_laptop)

# symmetric difference
unique = mobile_unbox.symmetric_difference(laptop_unbox)
print(unique)