# A company checks performance:
#     + KPI ≥ 80 → “Excellent”
#     + 60 ≤ KPI < 80 → “Good”
#     + 40 ≤ KPI < 60 → “Average”
#     + else → “Poor”
# Write full if-elif-else structure.
sales = int(input(f'Sales : '))
cost = int(input(f'Cost : '))
KPI = ((sales - cost)*100) / cost
if KPI >= 80:
    print("EXCELLENT")
elif ( 60 <= KPI < 80):
    print(f'GOOD')
elif ( 40 <= KPI < 60):
    print("AVERAGE")
else:
    print(f'POOR') 
