import SALES_ENGINE     # importing functions 

# the data sets
products = ["Laptop","Phone","Tablet","Monitor","Keyboard","Mouse"]
prices = [60000,25000,15000,12000,2000,800]
quantity = [5,10,7,4,20,25]
discount = [10,5,15,8,0,0]

# assigning list to variables
data = SALES_ENGINE.SalesAnalytics(products, prices, quantity, discount)

# calling fianl report
data.generate_report()

# calling top selling 
print("\nHIGH REVENUE PRODUCTS")
for rank , (product, rev) in enumerate(data.high_revenue_products(),start=1):
    print(f'{rank} -> {product}')

# ranking the report
data.rank_products()    

# per product final amount after discount     --\
# print(data.calculate_final_prices())          |
#                                               |==> for code 
# per product Revenue                           |    checking
# print(data.calculate_revenue())             --/    error 
