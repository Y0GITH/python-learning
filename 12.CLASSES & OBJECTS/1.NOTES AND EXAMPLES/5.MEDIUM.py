# Create a class Product
#     attributes: name, price
#     method: display_info()

class Product:
    def __init__(self , name , price):
        self.name = name
        self.price = price

    def info(self):
        return f'{self.name} is ${self.price}.'    

a = Product('apple' , 1000)
print(a.info())