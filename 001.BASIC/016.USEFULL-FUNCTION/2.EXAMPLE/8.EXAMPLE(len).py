#🔹 8️⃣ len() — Data Validation
#You received a dataset of customer names:
#   customers = ["Ravi", "Anita", "Suresh", "Meena", "Rahul","Kiran"]
#Task:
#    Use len() to print:
#        Total customers: X
#    Then check if the dataset has more than 5 customers.
customers = ["Ravi", "Anita", "Suresh", "Meena", "Rahul","Kiran"]
total_customer = len(customers)
print(f'Total number of customer : {total_customer}',end=' :: ')
if total_customer > 5:
    print(f'Data has more than 5 customer.')
else:
    print(f'Data has less than 5 data.')
