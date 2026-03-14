# Given a 2D list:
# matrix = [
#     [10, 20, 30],
#     [40, 50, 60]
# ]
# Print each row and each value using nested loops.
matrix = [
     [10, 20, 30],
     [40, 50, 60]
 ]
for row in matrix:
    for value in row:
        print(f'{value}',end=" ")
    print()    
    