class SalesAnalyzer:
    def __init__(self, sales):
        self.sales = sales

    def total(self):
        total = 0
        for s in self.sales:
            total += s
        return total

    def average(self):
        return self.total() / len(self.sales)

sales_data = SalesAnalyzer([1200, 1500, 900])
print(sales_data.total())
print(sales_data.average())
