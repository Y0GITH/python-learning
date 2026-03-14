# Count how many rows in the table have the column empty (NULL).
# sql query = select count(*) from tabls where column is null;
# above a sql query to check how may data are empty  
tables = ['customers','orders','products','prices']
columns = ['id','create_data']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')
# now python will automate a set of lines to find it         