# Write a function that takes total sales and number of days as input and returns the average daily sales.
def average_sales(total_sales,number_of_days):
    average_sales=total_sales/number_of_days
    return round(average_sales)
a = int(input(f'Enter the total sales : '))
b = int(input(f'Enter the number of days : '))
print("average sales is $",average_sales(a,b))
