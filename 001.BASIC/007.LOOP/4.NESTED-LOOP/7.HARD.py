# Compare all values in the list and print duplicates using nested loops (without using count() or sets):
# data = [10, 20, 10, 30, 20, 40]
# Expected output: Duplicate found: 10
#                  Duplicate found: 20

# data = [10, 20, 10, 30, 20, 40]
# duplicates = []
# for i in range(len(data)):
#     for j in range(i+1,len(data)):
#         if data[i] == data[j] and (data[i] not in duplicates):
#             duplicates.append(data[i])
# for value in duplicates:
#     print(f'duplicate found : {value}')  
              
data = [10, 20, 10, 30, 20, 40]
duplicates = []
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i] == data[j] and (data[i] not in duplicates):
            duplicates.append(data[i])
for value in duplicates:
    print(f'Duplicate found : {value}')        
print(range(3))    