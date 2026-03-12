# 🔹 1️⃣2️⃣ COMBINED CHALLENGE (VERY HARD)
# Dataset:
#     products = ["Laptop", "Phone", "Tablet", "Monitor"]
#     prices = [60000, 25000, 15000, 12000]
#     discount = [10, 5, 15, 8]
# Tasks:
#     1️⃣ Use zip() to combine data
#     2️⃣ Use map() + lambda to calculate discounted price
# Formula:
#     price - (price * discount / 100)
# 3️⃣ Print result:
#     Laptop → 54000
#     Phone → 23750
#     Tablet → 12750
#     Monitor → 11040
products = ["Laptop", "Phone", "Tablet", "Monitor"]
prices = [60000, 25000, 15000, 12000]
discount = [10, 5, 15, 8]
bill = list(map(lambda price,rate: round(price-(price*(rate/100))),prices,discount))
data = list(zip(products,prices,discount,bill))
for product,price,rate,end in data:
    print(f'{product} -> {end}')
