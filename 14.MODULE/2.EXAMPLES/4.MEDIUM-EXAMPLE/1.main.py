# Create module transactions.py with a function convert_to_int()
# Input: ["100", "200", "450"]
# Output: [100, 200, 450]
# Use full module import.
import transactions
data = ["100", "200", "450"]
cleaned_data = transactions.convert_to_int(data)
print(f'Before : {data}\nAfter : {cleaned_data}')