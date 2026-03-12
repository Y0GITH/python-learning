class student:
    def __init__(self , n , a):
        self.name = n
        self.age = a
        print(f'{self.name} is {self.age} year old.')

a = student('Yogith',23)
try:
    a = student()        
except:
    print(f'there is error')