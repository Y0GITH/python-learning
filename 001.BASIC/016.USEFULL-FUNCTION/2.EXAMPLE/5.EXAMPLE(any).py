# 🔹 5️⃣ any() — Risk Detection
# A company wants to know if any transaction exceeds ₹10,000.
# Dataset:
#     transactions = [2000, 4500, 9800, 12000, 3000]
# Task:
#     Use any() to check:
#         transaction > 10000
# Print:
#     "High risk transaction detected"
#     or
#     "No high risk transaction"
transactions = [2000, 4500, 9800, 12000, 3000]
check = any(transaction > 10000 for transaction in transactions)
if check:
    print(f'High risk transaction detected')
else:
    print(f'No high risk transaction')    