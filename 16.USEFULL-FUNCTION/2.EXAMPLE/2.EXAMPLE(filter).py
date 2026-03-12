# 🔹 2️⃣ filter() — Fraud Detection
# You are analyzing transactions.
# Dataset:
#     transactions = [120, 5000, 300, 7200, 450, 9000, 800]
# Task:
#     Using filter() + lambda, extract only suspicious transactions.
# Condition:
#     transaction > 5000
# Store them in:
#     fraud_transactions
transactions = [120, 5000, 300, 7200, 450, 9000, 800]
fraud_transactions = list(filter(lambda x: x>5000,transactions))
print(f'Fraud Transactions : {fraud_transactions}')