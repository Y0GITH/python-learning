# Write a program to find the highest number in a list using a for loop.
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f'{max}')        