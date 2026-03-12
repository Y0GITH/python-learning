# transform a string list to float 
# price = ['$12.50', '$9.99', '$100.00']
price = ['$12.50', '$9.99', '$100.00']
new_price = list(map(lambda x: float(x.replace('$','')),price))
print(f'New list : {new_price}')
print(type(new_price[0]))