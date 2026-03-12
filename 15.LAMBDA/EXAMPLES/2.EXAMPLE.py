# Create a lambda function that calculates total revenue:
price = [100,200,300,400]
quantity = [2,4,6,8]
total_revenue = list(map(lambda x,y:x*y,price,quantity))
print(f'Total Revenue : {total_revenue}')