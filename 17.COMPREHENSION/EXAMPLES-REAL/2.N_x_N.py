# i want 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)   

# using lambda
# my_list = list(map(lambda n:n*n,nums))

my_list = [n*n for n in nums] 
print(my_list) 

