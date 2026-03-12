# creating a function to greet 
def greet(name):
    print(f'> hello {name.upper()}\n>Welcome to python \n>lets start coding :)')
name = input(f'>Enter your name : ')
message = input(f'> Type start to code :) ').upper()
if message == 'START':
    greet(name)
       