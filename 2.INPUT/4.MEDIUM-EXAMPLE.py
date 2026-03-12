# Take marks of 5 subjects as input and calculate the average marks.

# bad code
# English = int(input(" Enter English scored Marks : "))
# Kannada = int(input(" Enter Kannada scored Marks : "))
# Maths = int(input(" Enter Maths scored Marks : "))
# Science = int(input(" Enter Science scored Marks : "))
# Social = int(input(" Enter Social scored Marks : "))
# average = (English + Kannada + Maths + Science + Social)/5
# print(" the average of all subgect is ",average)

marks = list(
    map(
        int, 
        input(f'Enter the marks one by one with space : ').split()
        )
        )
average_marks = sum(marks)/len(marks)
print(f'Average marks of {len(marks)} subjects in {average_marks}.')