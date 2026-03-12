# Given a list of monthly expenses:
# expenses = [2500, 1800, 3200, 1500, 2700]
# Using a for loop, calculate:
#   Total expense
#   Average expense
# (Do NOT use sum())
expenses = [2500, 1800, 3200, 1500, 2700]
total_expence = 0
for expence in expenses:
    total_expence += expence
print(f'Total expenses : {total_expence}')
print(f'Average expenses : {total_expence/len(expenses)}')     