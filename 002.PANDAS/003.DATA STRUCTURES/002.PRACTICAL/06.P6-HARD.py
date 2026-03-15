# 6️⃣ Create a sales DataFrame with:
#     Product
#     Price
#     Quantity
#     Revenue
# Calculate revenue manually while creating the dataset.
import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [800, 20, 50],
    "Quantity": [2, 5, 3]
}
df = pd.DataFrame(data)
df['Revenue'] = df['Price']*df['Quantity']
print(df)