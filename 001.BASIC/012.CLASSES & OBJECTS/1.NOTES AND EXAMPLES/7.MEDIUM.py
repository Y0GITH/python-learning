# Create a class SalesData
#     attribute: list of sales
#     method: total_sales()
#     method: average_sales()
class SalesData:
    def __init__(self , sales):
        self.sales = sales

    def total_sales(self):
        total_sales = 0
        for sale in self.sales:
            total_sales += sale
        return total_sales

    def average_sales(self):
        return sum(self.sales)/len(self.sales)

sales = SalesData([1200,2300,1400])
print(f'Total Sales : {sales.total_sales()}')        
print(f'Average Sales : {round(sales.average_sales())}')        