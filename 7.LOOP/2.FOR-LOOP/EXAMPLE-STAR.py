# print stars in specification
# expected output :
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *
size = 10
for i in range(size):
    count = size - i
    print(f'{'*'*count}')
