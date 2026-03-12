# From the dictionary below, find the highest price using a loop:
# products = {
#     "Laptop": 55000,
#     "Mobile": 20000,
#     "Tablet": 30000,
#     "Headset": 3000
# }
# Expected:
# Highest price: 55000 (Laptop)

# my code
# products = {
#     "Laptop": 55000,
#     "Mobile": 20000,
#     "Tablet": 30000,
#     "Headset": 3000
# }
# highest = 0
# product = ""
# 
# for x,y in products.items():
#     if  y > highest:
#         highest = y 
#         product = x
# print(f'Highest price: {highest} ({product})')        

# better way 
products = {
    "Laptop": 55000,
    "Mobile": 20000,
    "Tablet": 30000,
    "Headset": 3000
}

# initialize with first product
product_list = list(products.items()) # 2 dimension
product, highest = product_list[0]

for name, price in product_list[0:]:   # start from second item
    if price > highest:
        highest = price
        product = name

print(f'Highest price: {highest} ({product})')
