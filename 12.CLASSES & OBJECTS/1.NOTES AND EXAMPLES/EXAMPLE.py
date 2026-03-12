class Person:
    def __init__(self , name):
        self.name = name
        
    def talk(self):
        return f'hi, I am {self.name}.'

person1 = Person('yogith')
print('1',person1.name)   
print(person1.talk())   

person2 = Person('anu')
print('1',person2.name)   
print(person2.talk())    
