class SalesAnalytics:   # CREATING A CLASS
    def __init__(self, products, prices, quantity, discount):
        self.products = products    # Assigning objests
        self.prices = prices
        self.quantity = quantity
        self.discount = discount

    def calculate_final_prices(self): # compute final price
        final_prices = list(map(    # using map + lamda
            lambda price, rate: round(price-(price*rate/100)),
            self.prices,self.discount))
            # formula : Price - Discount Amount 
        return final_prices  
    
    def calculate_revenue(self):    # creating revenue
        revenue = list(map(
            lambda price , quantity: price*quantity,
            self.prices,self.quantity))    
            # formula : price x quantity  (ignoring)
        return revenue

    def generate_report(self):      
        final_prices = self.calculate_final_prices()
        revenue = self.calculate_revenue()
        # i felt to rename cal_revenue as revenue but dont have time             

        print("PRODUCT SALES REPORT")
        print("---------------------")

        for product,price,qty,final,rev in zip(self.products,
                                               self.prices,
                                               self.quantity,
                                               final_prices,
                                               revenue):
            print(f"{product} → Price:{price} → Qty:{qty} → Final:  {final} → Revenue:{rev}")

    def high_revenue_products(self):
        revenue = self.calculate_revenue()
        high_products = list(filter(lambda item: item[1] > 100000,
                zip(self.products, revenue)))
        # "item[1] > 100k" cauz we ziped product & revenue of each and revenue is relationaly dependent on product 
        return high_products    
    
    def rank_products(self):
        revenue = self.calculate_revenue()
        data = list(zip(self.products, revenue))
        sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
        # sorting based on revenue, so x[1]. as revenue index is 1 
        print("\nTOP PRODUCTS BY REVENUE")
        for rank, (product, rev) in enumerate(sorted_data, start=1):
            print(f"{rank} → {product} → {rev}")
