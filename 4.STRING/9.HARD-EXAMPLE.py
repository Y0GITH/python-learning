# "Transaction ID: TXN93482 — Status: SUCCESS — Amount: ₹2500"
# Write a condition using only in to check:
#     If the transaction is successful
#     If the transaction contains a valid ID starting with 'TXN'
#     If the string contains the currency symbol ₹
# Do not use .find(), slicing, or regex — ONLY in.
# a="Transaction ID: TXN93482 — Status: SUCCESS — Amount: ₹2500"
# x,y,z=a.split("—")
# if "TXN" in x and "SUCCESS" in y and "₹" in z:
#     print("the transaction is successful")
# else:
#     print("there is a error in transaction")
    
data = "Transaction ID: TXN93482 — Status: SUCCESS — Amount: ₹2500"
parts = data.split(' — ') 
transaction_dect = {}
for item in parts:
    key, value = item.split(': ')
    transaction_dect[key] = value
if "SUCCESS" in transaction_dect["Status"] and "TXN" in transaction_dect["Transaction ID"] and "₹" in transaction_dect["Amount"]:
    print(f'The transaction is Sucessful and valid.')