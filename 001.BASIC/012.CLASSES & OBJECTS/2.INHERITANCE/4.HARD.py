# Parent Class: SalesReport
#     + attribute: sales (list of numbers)
#     + method: total_sales()
#     + method: highest_sale()
# Child Class: DetailedReport (inherits SalesReport)
#     + method: average_sale()
#     + method: lowest_sale()
#     + method: show_summary()
# → This should print a summary containing:
#     + Total
#     + Highest
#     + Average
#     + Lowest
class SalesReport:
    def __init__(self, sales):
        self.sales = sales

    def total_sales(self):
        total_sales = 0
        for sale in self.sales:
            total_sales += sale
        return total_sales 
                   
    def highest_sale(self):
        highest_sale = self.sales[0]
        for sale in self.sales:
            if sale > highest_sale:
                highest_sale = sale
        return highest_sale
    
class DetailReport(SalesReport):
    def average_sales(self):
        average_sales = self.total_sales() / len(self.sales)
        return average_sales

    def lowest_sale(self):
        lowest_sale = self.sales[0]
        for sale in self.sales:
            if sale < lowest_sale:
                lowest_sale = sale
        return lowest_sale 

    def show_summary(self):
        print(f'Total Sales : {self.total_sales()}')  
        print(f'Average Sales : {round(self.average_sales())}')  
        print(f'Highest Sales : {self.highest_sale()}')  
        print(f'Lowest Sales : {self.lowest_sale()}')

data = DetailReport([1000,5000,2000,7000,100000])
data.show_summary()