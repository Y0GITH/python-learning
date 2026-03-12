# find the lowest number in the list
numbers = [2,5,1,3,7,5,8]
min = numbers[0]
for number in numbers:        
    if number < min:
        min = number
print(min)        