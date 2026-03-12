# You have:
# data = [10, 20, 10, 30, 20, 40, 30]
# Using ONLY a loop (no set, no count):
# Print unique numbers only once
# Expected output: Unique: 10
#                  Unique: 20
#                  Unique: 30
#                  Unique: 40
datas = [10, 20, 10, 30, 20, 40, 30]
unique = []
for data in datas:
    if data not in unique:
        unique.append(data)
for data in unique:
    print(f'unique : {data}')        
    