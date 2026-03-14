# print stars on specification
# expected output :
size = 10
for i in range(size):
    count = size - i
    print(f'{(' '*i) + ('*'*count)}')
for i in range(size):
    count = size - i
    print(f'{(' '*(count-1)) + ('*'*(i+1))}')