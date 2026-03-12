# 🔹 7️⃣ sorted() — Leaderboard System
# You have sales numbers:
#     sales = [4500, 7000, 3200, 8900, 6100]
# Task:
#     1️⃣ Sort the sales in descending order
#     2️⃣ Print the top 3 sales values
# Example output:
#     Top Sales:
#             8900
#             7000
#             6100
sales = [4500, 7000, 3200, 8900, 6100]
highest_sales = sorted(sales, reverse= True)
print(f'Top Sales :')
for i in range(3):
    print(highest_sales[i])