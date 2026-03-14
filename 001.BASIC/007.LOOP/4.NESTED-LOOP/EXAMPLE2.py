# creat a files for 28 days of jan and feb in the year 2026 and 2027
years = [ 2026 , 2027 ]
months = [ 'jan' , 'feb' ]
days = range(1,29)
for y in years:
    for m in months:
        for d in days:
            print(f'report_{d}_{m}_{d}.csv')