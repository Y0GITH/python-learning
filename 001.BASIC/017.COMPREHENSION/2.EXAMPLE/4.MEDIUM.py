# Dataset:
#     prices = [100,200,300]
#     qty = [2,3,4]
# Create a list of revenues.
prices = [100,200,300]
qty = [2,3,4]
revenue = [p*q for p,q in zip(prices,qty)]
print(*[f'Price: {p}, Quantity: {q}, Revenue: {r}' for p,q,r in zip(prices,qty,revenue)],sep='\n')
# * is used for unpacking 
