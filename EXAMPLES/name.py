a = input(f'enter ur name : ')
id1 = ''
id2 = ''
for index in range(len(a)):
    if index % 2 == 0:
        id1 += '_'
    else:
        id1 += a[index]
print(id1)
for index in range(len(a)):
    if index % 2 == 0:
        id2 += a[index]
    else:
        id2 += '_'
print(id2)