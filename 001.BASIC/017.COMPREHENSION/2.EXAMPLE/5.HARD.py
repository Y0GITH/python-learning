# Dataset:
#     products = ["Laptop","Phone","Tablet"]
#     prices = [60000,25000,15000]
#     discount = [10,5,15]
# Using list comprehension + zip, calculate final prices after discount.

products = ["Laptop","Phone","Tablet"]
prices = [60000,25000,15000]
discount = [10,5,15]

final = [p-(p*d/100) for p,d in zip(prices,discount)]

data = zip(products,prices,discount,final)
print(*[f'Product: {pd}, Price: {p}, Discount: {d}, Bill: {f}' for pd,p,d,f in data],sep='\n')