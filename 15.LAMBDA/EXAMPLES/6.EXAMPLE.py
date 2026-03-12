# Use lambda with filter() to return sales greater than 1000.
sales = [500, 1200, 700, 1800, 400]
high_sales = list(filter(lambda x: x>1000,sales))
print(f'High Sales : {high_sales}')
