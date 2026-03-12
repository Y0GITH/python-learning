class RetailAnalytics:
    def __init__(self,transactions):
        self.transactions = transactions

    def claculate_revenue(self):
        revenue_data = []
        for tid, product, category,price,qty in self.transactions:
            revenue = price*qty
            revenue_data.append((product,category,revenue))  
        return revenue_data
    
    def total_revenue(self):
        total = 0
        for tid,product,category,price,qty in self.transactions:
            total+= price*qty
        return total

    def high_revenue_transactions(self):
        revenue_data = self.claculate_revenue()
        high_sales = list(filter(lambda x:x[2]>50000,revenue_data))
        return high_sales

    def category_revenue(self):
        category_total = {}
        for tid, product,category,price,qty in self.transactions:
            revenue= price*qty
            if category not in category_total:
                category_total[category] = 0
            category_total[category] += revenue
        return category_total
    
    def rank_products(self):
        revenue_data = self.claculate_revenue()
        sorted_products = sorted(revenue_data,key=lambda x: x[2],reverse=True)
        for rank,item in enumerate(sorted_products,start=1):
            print(f'{rank} → {item[0]} → {item[2]}')
    
    def generate_report(self):
        print("\nRETAIL SALES REPORT")
        print("-------------------")
        revenue_data = self.claculate_revenue()
        for product,category,revenue in revenue_data:
            print(f'{product} → Category:{category} → Revenue:{revenue}')