# i want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

# my_list = []
# for letter in 'ab':
#     for num in range(2):
#         my_list.append((letter,num))
# print(my_list) 

my_list = [(let,num) for let in 'ab' for num in range(2)]
print(my_list)