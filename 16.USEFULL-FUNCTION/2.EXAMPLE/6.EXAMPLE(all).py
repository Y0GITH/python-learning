# 🔹 6️⃣ all() — Employee Performance
# A manager wants to check if all employees met their sales target.
#     Target = ₹5000
# Dataset:
#     sales = [5200, 6100, 5800, 4900]
# Task:
#    Use all() to check if every employee's sales is greater than 5000.
# Print:
#     All targets achieved
#     or
#     Targets not achieved
sales = [5200, 6100, 5800, 4900]
check = all(sale > 5000 for sale in sales)
if check:
    print(f'All targets achieved')
else:
    print(f'Targets not achieved')    