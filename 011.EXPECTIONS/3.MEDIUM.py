# Write a program that:
#     Takes two numbers
#     Divides them
#     Handles ZeroDivisionError
try:
    def devision(a,b):
        return round(a/b)
    a = int(input(f'Fix value of "A" : '))
    b = int(input(f'Fix value of "B" : '))
    result = devision(a,b)
    print(result)
except ZeroDivisionError:
    print(f'You cant assign "0" is input') 
else:
    print(f'program executed sucessfully.')
    