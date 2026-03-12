# Write a function is_even(n) that returns:
# True if the number is even
# False if the number is odd
def is_even(n):
    if n%2 == 0:
        print(f'the number is even.')
    else:
        print(f'the number is odd.')
n = int(input(f'Enter the number : '))
is_even(n)
