# 🔹 3️⃣ zip() — Product Sales Report
# You have two datasets:
#     products = ["Apple", "Mango", "Banana", "Orange"]
#     sales = [1200, 1500, 900, 2000]
# Task:
# Using zip(), print a report like:
#     Product : Apple , Sales : 1200
#     Product : Mango , Sales : 1500
#     ...
# Then create a list called:
#     product_sales
# which contains tuples like:
#     ("Apple",1200)
products = ["Apple", "Mango", "Banana", "Orange"]
sales = [1200, 1500, 900, 2000]
product_sales = zip(products,sales)
for product,sale in product_sales:
    print(f'Product : {product} , Sales : {sale}')