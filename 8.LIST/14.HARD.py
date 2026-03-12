# Given a matrix:
# data = [
#     [10, 20, 10],
#     [30, 20, 40],
#     [50, 10, 60]
# ]
# Using nested loops only, find all unique values in the matrix.
# Example output:Unique: 10
#                Unique: 20
#                Unique: 30
#                Unique: 40
#                Unique: 50
#                Unique: 60
datas = [
    [10, 20, 10],
    [30, 20, 40],
    [50, 10, 60]
]
unique = []
for data in datas:
    for value in data:
        if value not in unique:
            unique.append(value)
for value in unique:
    print(f'unique: {value}')            