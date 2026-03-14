# Keep asking for daily sales until the user enters "done".
# Then print the total sales.
total_sales = 0
while True:
    sales = int(input(f'Enter the sales : '))
    total_sales += sales
    a = input(f'is sales done? [yes/no]').lower()
    if a == "yes":
        break
print(f'total sales : ${total_sales}')        