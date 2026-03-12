class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return 'Pass'
        else:
            return 'Fail' 

a = Student('Yogith',80)
print(f'{a.result()}')
