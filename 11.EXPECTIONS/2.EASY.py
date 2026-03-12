# Write a program that:
#     Takes a number from user
#     Handles ValueError if user enters text
try:
    number = int(input(f'Enter a Number : '))
except ValueError:
    print(f'Invalide input')
else:
    print(f'program executed sucessfully.')
        