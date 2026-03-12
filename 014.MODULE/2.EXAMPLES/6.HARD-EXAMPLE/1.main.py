# Create product.py with
# Parent: Product
# Child: DiscountProduct (overrides final_price)
# Import child class, calculate discounted price.
import product as function

product1 = function.DiscountProduct('apple',10000,10)
product2 = function.DiscountProduct('mango',20000,20)
print(f'{product1.name} after discount of {product1.discount}% is {round(product1.final_price())}/-')
print(f'{product2.name} after discount of {product2.discount}% is {product2.final_price()}/-')
