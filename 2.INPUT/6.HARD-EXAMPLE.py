# Take 3 product prices as input and calculate:
# Total price
# Average price
product_A = int(input("entre the product A price : "))
product_B = int(input("entre the product B price : "))
product_C = int(input("entre the product C price : "))
total_price = (product_A + product_B + product_C)
avg_price =  int((product_A + product_B + product_C)/3)
print("total price is ",total_price," and average price is ",avg_price)
