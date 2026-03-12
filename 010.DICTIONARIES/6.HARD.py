# Given a dictionary of marks:
# marks = {"Eng": 80, "Math": 70, "Sci": 90}
# Find the average marks using loop.

# marks = {"Eng": 80, "Math": 70, "Sci": 90}
# total_marks = 0
# subjects = []
# for x,y in marks.items():
#     subjects.append(x)
#     total_marks += y
# average_marks = total_marks/len(marks)
# print(f'average marks of {subjects} is {average_marks} ')    

# or better verstion

marks = {"Eng": 80, "Math": 70, "Sci": 90}

subjects = tuple(marks.keys())     # ('Eng', 'Math', 'Sci')
total_marks = sum(marks.values())  # 80 + 70 + 90
average_marks = total_marks / len(marks)
subject_string = ", ".join(subjects)  # joins the string so better out put   
print(f'Average marks of {subject_string} is {round(average_marks)}.')
