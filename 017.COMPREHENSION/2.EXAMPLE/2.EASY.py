# Create a list containing only numbers greater than 20.
data = [10,15,20,25,30]
new_data = [n for n in data if n>20]
print(f'Filtered data : {new_data}')