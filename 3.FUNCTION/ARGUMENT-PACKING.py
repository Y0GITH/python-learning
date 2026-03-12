# using function write a code where u pack and tupple 
def add_numbers(*num):
    # total = 0
    # for n in num:
    #     total += n
    total = sum(num)
    print(total)
add_numbers(2,3,4) 
add_numbers(1,2,43,5,5,3)       