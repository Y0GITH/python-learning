 #2️⃣ Create a Series with custom index:
 #    Mon Tue Wed
 #Values should represent daily sales.
import pandas as pd

data = [100,150,300]
df = pd.Series(data,index=['Mon','Tue','Wed'])
print(f'Dialy Sales : ')
print(df)