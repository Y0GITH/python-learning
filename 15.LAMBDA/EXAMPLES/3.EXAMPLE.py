# Using lambda, classify sales:
#     > 1000 → "High"
#     ≤ 1000 → "Low"

# sales = [500, 750, 1000, 1250, 1500]
# check = list(map(lambda x : 'High Sales' if x>1000 else 'Low sales', # sales ))
# for i in range(len(sales)):
#     print(f'Sales : {sales[i]} , Status : {check[i]}')

# better way 
sales = [500, 750, 1000, 1250, 1500]
check = list(map(lambda x: 'High Sales' if x > 1000 else 'Low Sales', sales))
for s, c in zip(sales, check):
    print(f"Sales : {s} , Status : {c}")
    