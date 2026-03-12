# using a function u need to creat a dictionari and add data to it
def create_dictionary():
    data = {}
    count = int(input(f'How many items do you want to add? : '))
    for i in range(count):
        key = input(f'Enter key {i+1}: ')
        value = input(f'Enter value for {key} : ')
        data[key] = value
    return data
result = create_dictionary()
print(f'Your dictionary:')
print(result)  
