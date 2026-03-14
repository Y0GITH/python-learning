data = {}
no_subject = int(input(f'select the number of subjects : '))
for i in range(no_subject):
    subject = input(f'Enter the {i+1} Subject : ').upper()
    marks = int(input(f'Enter the Marks in {subject} : '))
    data[subject] = marks
total_marks = 0 
for subject,marks in data.items():
    print(f'Marks scored in {subject} is {marks}')
    total_marks += marks 
average_marks = round(total_marks/no_subject)
print(f'-----------------------------------------------------------')
print(f'Total Marks is {total_marks}')
print(f'Average marks is {average_marks} %')    
print(f'-----------------------------------------------------------')