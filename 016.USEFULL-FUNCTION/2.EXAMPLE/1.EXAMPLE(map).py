# 🔹 1️⃣ map() — Salary Adjustment
# A company wants to increase employee salaries by 12%.
# Using map() + lambda, create a new list called updated_salaries.
salaries = [25000, 32000, 28000, 40000, 35000]
new_salary = list(map(lambda x:round(x*1.12),salaries))
print(f'New Salary : {new_salary}')