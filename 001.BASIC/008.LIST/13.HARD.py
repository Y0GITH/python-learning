# Given:
# sales = [
#     [120, 180, 200],
#     [90, 140, 160],
#     [200, 300, 250]
#         ]
# Calculate:
#     + Total sales per row
#     + Total sales for all rows
#     + Highest value in the entire matrix

sales = [
    [120, 180, 200],
    [90, 140, 160],
    [200, 300, 250]
]
total_sales = 0
max = sales[0][0]
i = 1
for sale in sales:
    row_total = 0
    for value in sale:
        row_total += value
        total_sales += value
        if value > max:
            max = value
    print(f'Row {i} total : {row_total}')
    i+=1        
print(f'total sales : {total_sales}\n highest sales : {max}')            