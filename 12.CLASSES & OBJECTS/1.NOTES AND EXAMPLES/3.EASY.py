# Create a class Car
#     attribute: brand
#     method: display_brand()

class Car:
    def __init__(self , brand ):
        self.brand = brand
        print(f'{brand}')

a = Car('BMW')