# You have a list of transactions:
# transactions = [120, -50, 340, -200, 560, -30]
# Using a for loop:
#   Count how many are credits (positive)
#   Count how many are debits (negative)
# Find total balance

transactions = [120, -50, 340, -200, 560, -30]
positive = 0
negative = 0
balance = 0
for i in transactions:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    balance += i    
print(f'number of credit : {positive}')            
print(f'number of debit : {negative}')            
print(f'balance : {balance}')