# Create a class Student
#     attributes: name, marks
#     method: check_pass()
#     (pass if marks ≥ 40)
class Student:
    def __init__(self , name , marks ):
        self.name = name
        self.marks = marks
        print(f'{(self.name).upper()} has got {self.marks}.')

    def check_pass(self):
        if self.marks >= 40:
            return 'pass'
        else:
            return 'fail'
            
a = Student('yogith' , 80)            
print(a.check_pass())