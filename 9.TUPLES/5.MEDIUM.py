# Given a list of tuples:
#     data = [(5, 10), (20, 30), (40, 50)]
# Print each pair using unpacking:
#     5 + 10 = 15
#     20 + 30 = 50
#     ...
data = [(5, 10), (20, 30), (40, 50)]
for x,y in data:
        print(f'{x} + {y} = {x + y}')