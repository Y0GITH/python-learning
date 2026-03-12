class Student:
    name = 'Yogith'
    age = 21
    def info(self):
        print(f'{self.name} is {self.age} year old.')
a = Student()
a.info()    #  Yogith is 21 year old.
a.name = 'Anu'
a.age = 20
a.info()    # Anu is 20 year old.
b = Student()
b.name = 'Ram'
b.age = 23
print(b.name,b.age)  # Ram 23
