# 5️⃣ Create a Series representing daily revenue for:
#     Mon Tue Wed Thu Fri
import pandas as pd

revenue = [100,200,150,300,400]
days = ['Mon','Tue','Wed','Thu','Fri']
df = pd.Series(revenue,index=days)
print(f'Dialy Revenue')
print(df)