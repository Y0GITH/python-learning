# Create a function analyze_sales(sales)
# where sales is a list like:
# 
# sales = [1200, 1500, 900, 2000, 1000]
# 
# Your function must return the following (using loops only):
#     Total sales
#     Average sale
#     Highest sale
#     Lowest sale
# ❌ Do NOT use built-in functions:
#     sum()
#     max()
#     min()
# ✔ Use loops only.
def result(sales):
    total_sales = 0
    highest_sales = sales[0]
    lowest_sales = sales[0]

    for i in sales:
        total_sales += i
    
        if i > highest_sales:
            highest_sales = i
    
        if i < lowest_sales:
            lowest_sales = i
    
    average_sales = total_sales/len(sales)
    
    print(f'total sales : {total_sales}')
    print(f'average sales : {round(average_sales)}')
    print(f'highest sales : {highest_sales}')
    print(f'lowest sales : {lowest_sales}')
    return

sales = [1200, 1500, 900, 2000, 1000]
result(sales)