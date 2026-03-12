# You have two lists:
# regions = ["North", "South"]
# products = ["Laptop", "Mobile", "Tablet"]
# Using nested loops, print combinations like:
# output: North - Laptop
#         North - Mobile
#         ...
#         South - Tablet

regions = ["North", "South"]
products = ["Laptop", "Mobile", "Tablet"]
for region in regions:
    for product in products:
        print(f'{region} - {product}')