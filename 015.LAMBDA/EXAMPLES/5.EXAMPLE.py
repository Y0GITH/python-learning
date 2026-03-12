# Use lambda with map() to calculate discounted prices.
# Formula:
#     final_price = price - (price * discount / 100)
prices = [1000, 2000, 3000]
discount = 10
end_price = list(map(lambda x : x-(x*(discount/100)), prices))
for a,b in zip(prices,end_price):
    print(f'Actual Price : {a} , Discount : 10% , Bill Amount {b}')