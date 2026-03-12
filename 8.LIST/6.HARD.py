# You have a list of sales:
# sales = [1200, 1500, 900, 2000, 1000]
# Using a loop, calculate:
# total sales
# average sales
# (Don’t use sum() or len())

sales = [1200, 1500, 900, 2000, 1000]
total_sales = 0
for sale in sales:
    total_sales += sale
average_sales = total_sales/len(sales)
print(f'total sales : {total_sales}') 
print(f'average sales : {round(average_sales)}')   
