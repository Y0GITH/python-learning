# Ues pass the loop if there is a empty cell

# pass is used when u dont know what do do with if statement.
# so later we can change it 
names = ["YOGITH","RONLDO","MESSI"," ","KEVIN"]
for name in names:
    if name == " ":
        pass
    print(f'Name : {name}')

# now in real life 
# now i know what to do with to if condition    
# and now I'll come back to pass and edit the code 
# Ues continue the loop if there is a empty cell

# names = ["YOGITH","RONLDO","MESSI"," ","KEVIN"]
# for name in names:
#     if name == " ":
#         name = name.replace(" ","unknown")     <----
#     print(f'Name : {name}.') 