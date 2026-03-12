# Given:
# matrix = [
#     [10, 20, 30],
#     [40, 50, 60]
# ]
# Write code to print:
# 10 20 30
# 40 50 60
matrix = [
     [10, 20, 30],
     [40, 50, 60]
         ] 
for number in matrix:
    for n in number:
        print(f'{n}',end=" ")
    print()    