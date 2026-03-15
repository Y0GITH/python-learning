# 4️⃣ Create a DataFrame of employees:
#     Name
#     Department
#     Salary
# Print the DataFrame.
import pandas as pd
data = {
    'Name':['Ram','sam','tom'],
    'Department':['A','B','C'],
    'Salary':[10000,15000,20000]
}
df = pd.DataFrame(data)
print(df)