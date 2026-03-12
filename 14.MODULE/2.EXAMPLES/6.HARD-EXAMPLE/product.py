class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class DiscountProduct(Product):
    def __init__(self, name, price,discount):
        super().__init__(name,price)
        self.discount = discount

    def final_price(self):
        return self.price - (self.price*(self.discount)/100)

        