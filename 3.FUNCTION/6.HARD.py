# Write a function that:
#     Accepts a list of numbers
#     Returns the highest number
#     (Do NOT use max())
# Example:
# result = highest_value([10, 3, 50, 20])
# print(result)   # 50

# my code 
# def find_highest():
#     a=[]
#     while True:
#         num = (input(f'enter the number or type done : ')).lower()
#         if num == 'done':
#             break
#         else:
#             num = int(num)
#             a.append(num)
#     highest_num = a[0]        
#     for i in a:
#         if i > highest_num:
#             highest_num = i
#     print(f'Highest number : {highest_num}')
#     return
# find_highest()
# but when u enter done in the starting the code will return error 
# so a better code 

def find_highest():
    a = []
    while True:
        num = input(f'Enter a number (or tye "done") : ').lower()
        if num == 'done':
            break
        a.append(int(num))
    if len(a) == 0:
        print("No number entered.")
        return
    highest_num = a[0]
    for i in a:
        if i > highest_num:
            highest_num = i
    print(f'Highest number : {highest_num}')
    return
find_highest()            