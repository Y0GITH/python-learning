# loop through a list of days and print only the working days, skipping the weekends

# MY CODE
# days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
# for day in days:
#     if day == "SAT" or day== "SUN":
#         continue
#     print(f'{day} is a working day')

# use a define list variable in if condition 
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
weekend = ['SAT','SUN']
for day in days:
    if day in weekend:
        continue
    print(f'{day} is a working day')
