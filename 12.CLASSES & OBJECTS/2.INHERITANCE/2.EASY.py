# Create a parent class Employee with name & salary.
# Create a child class Manager that adds department.
class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def output(self):
        print(f'Name: {(self.name).title()}')    
        print(f'Salary: {self.salary}')    
        print(f'Department: {(self.department).upper()}')    

yogith = Manager('yogith',100000,'data analyst')
yogith.output()