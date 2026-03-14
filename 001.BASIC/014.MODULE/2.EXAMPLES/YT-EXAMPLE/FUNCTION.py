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

# Write a function calculate_total(p1, p2, p3)
# → return the total price of 3 products.
def  calculate_total():
    num = []
    total = 0
    for i in range(1,4):
        price = int(input(f'Enter the price of product {i}: '))
        num.append(price)
    # for x in num:
    #     total += x    
    total = sum(num)    # better
    return total
result = calculate_total()
print(f'Total = {result}')    

