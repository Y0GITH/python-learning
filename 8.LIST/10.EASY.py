# Print the first row and the second row separately.

matrix = [[1,2], [3,4], [5,6]]
for number in matrix:
    for n in number:
        print(f'{n}',end=" ")
    print()    