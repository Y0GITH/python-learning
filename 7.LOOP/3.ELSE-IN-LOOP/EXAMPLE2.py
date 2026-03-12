# check weather any filename appears more than once 
file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
seen = []
duplicates = []
for file in file_list:
    if file in seen:
        duplicates.append(file)
    else:
        seen.append(file)
print(f'Duplicates: {duplicates}')            