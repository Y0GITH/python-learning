# Ues continue the loop if there is a empty cell
names = ["YOGITH","RONLDO","MESSI"," ","KEVIN"]
for name in names:
    if name == " ":
        print(f'Empty cell detected!')
        continue
    print(f'Name : {name}.')