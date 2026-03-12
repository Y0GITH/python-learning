# Count how many times "apple" appears in this list:
# fruits = ["apple", "banana", "apple", "mango", "apple"]
fruits = ["apple", "banana", "apple", "mango", "apple"]
apple_count = 0
for fruit in fruits:
    if fruit == "apple":
        apple_count += 1
print(f'number of apples in data is : {apple_count}')        
