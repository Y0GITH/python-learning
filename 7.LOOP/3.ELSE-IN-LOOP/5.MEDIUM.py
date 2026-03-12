# Using a for loop:
# Search for "Python" in this list:
# ["Java", "C", "C++", "SQL"]
# Use loop–else to print "Found" or "Not Found".

datas = ["Java", "C", "C++", "SQL"]
for data in datas:
    if data == "Python":
        print(f'Found.')
        break
else:
    print(f'Not Found.')    
    