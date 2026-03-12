# Create a class Product
#     attributes: name, price
#     method: display_info()
class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary*12

a = Employee('YOGITH',45000)
print(a.annual_salary())            