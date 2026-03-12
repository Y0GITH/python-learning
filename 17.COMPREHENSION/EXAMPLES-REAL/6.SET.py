# with the help of set remove duplication
num = [4,3,4,5,5,6,7,6,8,7,9,9,1,1,2,1,3]

# my_set = set()
# for i in num:
#     my_set.add(i)
# print(my_set)

# my_set = list(set(num))
# print(my_set)    

my_set = {n for n in num}
print(my_set)    
