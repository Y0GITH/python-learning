# add if value in list is even 
nums = [1,2,3,4,5,6,7,8,9,10]

# data = []
# for i in nums:
#     if i%2==0:
#         data.append(i) 
# print(data)  

# data = list(filter(lambda x: x%2==0,nums))
# print(data)

data = [n for n in nums if n%2==0]
print(data)