# checking weather the file is csv or not.
# if the file is in csv then detect it and report it.
files = ['data1.csv','data2.csv','report.pdv','report2.csv','data3.txt']
non_csv_files = []
csv_files = []
for file in files:
    if not file.endswith('.csv'):
        non_csv_files.append(file)
    else:
        csv_files.append(file)
else:
    print(f'this are csv files : {csv_files} \n this are non csv files : {non_csv_files}')        

