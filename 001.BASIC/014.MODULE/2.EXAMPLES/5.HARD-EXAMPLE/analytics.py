class Analytics:
    def __init__(self, sales):
        self.sales = sales

    def total(self):
        total_sales = 0
        for sale in self.sales:
            total_sales += sale
        return total_sales

    def average(self):
        return sum(self.sales)/len(self.sales)