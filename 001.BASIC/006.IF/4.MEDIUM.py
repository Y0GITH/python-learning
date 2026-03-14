# A student passed if:
#   + marks ≥ 35 and
#   + attendance ≥ 75
# Write an if condition to check pass/fail.
marks = int(input(f'Enter the scored marks : '))
attendance = int(input(f'Enter the attendance percentage : '))
if (marks >= 35) and (attendance >= 75):
    print(f'The student has passed. :-)')
else:
    print(f'The student has failed. :-)')
