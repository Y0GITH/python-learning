# if name is less than 3 characters long 
#     name must be at least 3 characters 
# otherwise if it's more than 50 characters long 
#     name can be a maximum of 50 characters
# otherwise 
#     nam looks good!   

# what i did 
# name = input('Enter your name : ')
# leng = len(name)
# if leng < 3:
#     print(f' Name must be at least 3 characters. :-)')
# elif leng > 50: 
#     print(f' Name must be within 50 characters. :-)')
# else:
#     print(f'name looks goood! :-)')       

# improved 
name = input('Enter your name : ')
if len(name) < 3:
    print(f' Name must be at least 3 characters. :-)')
elif len(name) > 50: 
    print(f' Name must be within 50 characters. :-)')
else:
    print(f'name looks goood! :-)')  