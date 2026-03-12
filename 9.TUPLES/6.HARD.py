# Each tuple represents a product:
# products = [
#     ("Laptop", 55000, 10),
#     ("Mobile", 20000, 15),
#     ("Headset", 3000, 5)
# ]
# Unpack each tuple and print:
#     + product name
#     + price
#     + stock
#     + total value = price * stock
products = [
    ("Laptop", 55000, 10),
    ("Mobile", 20000, 15),
    ("Headset", 3000, 5)
]
for a,b,c in products:
    print(f'product name : {a}')
    print(f'price : {b}')
    print(f'stock : {c}')
    print(f'total value : {b*c}')