# A transaction list is given:
# transactions = [240, 180, -300, 420, -150]
# Check if any transaction amount is greater than 1000.
# If found → print "High value detected" and break.
# Else → print "All values normal".
transactions = [240, 180, -300, 420, -150]
for transaction in transactions:
    if transaction > 1000:
        print(f'High value detected.')
        break
else:
    print(f'All values normal.')    