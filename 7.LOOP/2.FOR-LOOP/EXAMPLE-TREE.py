# print a jesus tree
size = 29
space = round(size/2)
no_stars = 1
index = 0
wish = 'Merry Christmas'
wish = wish.upper()
while True:
    print(f'{wish[index]}',end=' ')
    index += 1
    print(f'{(' '*space)+('*'*no_stars)}')
    space -= 1
    no_stars += 2
    if no_stars > 29 or no_stars == 29:
        break
for i in range(2):
    print(f'{wish[13+i]}',end=' ')
    print(f'{(' '*13)+('|'*3)}')    
