# Dataset:
#     sales = [500,1200,700,1800,300]
# Create a list:
#     ["Low","High","Low","High","Low"]
# Condition:
#     >1000 → High
#     else → Low
sales = [500,1200,700,1800,300]
check = ['High' if n>1000 else 'Low' for n in sales]
print([f'{num} is {typ}' for num,typ in zip(sales,check)])
