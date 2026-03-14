# Create a class ExamAnalyzer
#     attribute: list of marks
#     method: highest_mark()
#     method: lowest_mark()
#     method: average_mark()
class ExamAnalyzer:
    def __init__(self , marks):
        self.marks = marks
    
    def hightest_marks(self):
        highest = self.marks[0]
        for mark in self.marks:
            if mark > highest:
                highest = mark
        return highest

    def lowest_marks(self):
        lowestest = self.marks[0]
        for mark in self.marks:
            if mark < lowestest:
                lowestest = mark
        return lowestest
    
    def average_mark(self):
        return round(sum(self.marks)/len(self.marks))
            
marks = [80,90,98]
data = ExamAnalyzer(marks) 
print(f'Highest Marks: {data.hightest_marks()}')
print(f'Lowest Marks: {data.lowest_marks()}')
print(f'Average Marks: {data.average_mark()}')
                         