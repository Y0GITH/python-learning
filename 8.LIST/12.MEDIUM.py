# Calculate the sum of all elements in the 2D list using nested # loops.
matrix = [
    [10, 20, 30],
    [40, 50, 60]
]
sum = 0
for n in matrix:
    for i in n:
        sum += i
print(f'sum of all : {sum}')        