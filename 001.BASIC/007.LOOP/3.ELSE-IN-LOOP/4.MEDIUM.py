# Ask user to enter 5 numbers.
# If any number is negative, break and print "Negative number found".
# Else after loop print "All numbers are positive".
for i in range(5):
    num = int(input(f'Enter a number : '))
    if num < 0 :
        print(f'negative number found.')
        break
else:
    print(f'All number are positive.')            