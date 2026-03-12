# A login system allows the user 3 chances to enter the correct password "admin".
# If correct → print "Welcome" and break.
# If all attempts fail → print "Account locked" using else after loop.
for i in range(3):
    password = input(f'enter the password : ')
    if password == "admin":
        print(f'Welcome.')
        break
    else:
        print(f'{2-i} chance remaining.')
else:
    print(f'Account locked.')    
    