# 3️⃣ Create a DataFrame with the columns:
#     Product
#     Price
#     Quantity
# Add at least 3 rows of data.
import pandas as pd
data = {
    'Product':['pen','pencil','key'],
    'Price':[10,5,20],
    'Quantity':[2,3,4]
}
df = pd.DataFrame(data)
print(df)