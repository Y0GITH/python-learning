def max_sales(sales):
    highest = sales[0]
    for sale in sales:
        if sale > highest:
            highest = sale
    return highest

def min_sales(sales):
    lowest = sales[0]
    for sale in sales:
        if sale < lowest:
            lowest = sale
    return lowest        