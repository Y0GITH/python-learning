# Dataset:
#     transactions = [200,5000,1200,300,7000]
# Create a list of only high transactions (>1000) and multiply them by 1.05 tax.
transactions = [200,5000,1200,300,7000]
taxed = [n*1.05 for n in transactions]
print(*[f'Transaction: {t}, Tax: {f-t}, Total Bill: {f}' for t,f in zip(transactions,taxed)],sep='\n')