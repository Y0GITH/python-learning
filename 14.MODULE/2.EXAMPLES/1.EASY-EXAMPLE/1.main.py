# Create a module cleaning.py with a function clean_names() that strips spaces & lowercases a list of names.
# Import it and clean:
# [" Alice ", "BOB ", " CharLie"]

import cleaning
data = ['  ANu   ','banu   ','RAMU','YoGiTh']
result = cleaning.clean_names(data)
print(f'before data : {data}\nafter data : {result}')
