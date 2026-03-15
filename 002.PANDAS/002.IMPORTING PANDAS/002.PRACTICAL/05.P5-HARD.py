# 6️⃣ Write a Python script that:
#     imports pandas
#     creates a DataFrame of 3 products and their prices
#     prints the DataFrame
import pandas as pd
data = {
    'Name':['pen','pencil','key'],
    'Price':[10,5,20],
    'Quantity':[2,3,4]
}
df = pd.DataFrame(data)
print(df)
