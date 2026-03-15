# 4️⃣ Write a Python program that:
# imports pandas
# creates a DataFrame with columns:
#     Product
#     Price
import pandas as pd

data = {
    'Product':['car','bike'],
    'Price':[200,100]
}
df = pd.DataFrame(data)
print(df)