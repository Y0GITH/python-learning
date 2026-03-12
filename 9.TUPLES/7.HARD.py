# Unpack this nested tuple without using indexing:
# t = (1, (2, 3), (4, (5, 6)))
# Extract: a = 1
#          b = 2
#          c = 3
#          d = 4
#          e = 5
#          f = 6
# (Use unpacking only.)
t = (1, (2, 3), (4, (5, 6)))
a, (b, c), (d, (e, f)) = t
print(f'{a}')
print(f'{b}')
print(f'{c}')
print(f'{d}')
print(f'{e}')
print(f'{f}')
