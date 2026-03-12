# A password system:
#  + User gets 3 attempts
#  + Correct password = "admin123"
#  + If correct → print "Access Granted"
#  + If 3 wrong attempts → print "Account Locked"  

# my code / but still can be better 
# attampt = 0
# max_attampt = 3
# while attampt < max_attampt:
#     password = input(f'Enter the password : ')
#     attampt += 1
#     if password == "admin123":
#         print(f'Access Granted.')
#         break
#     else:
#         print(f'Incorrect password. ')
#         print(f'only {(max_attampt+1) - attampt} remaining try ')
# if attampt == max_attampt:  # if this line is not there then we # still get account locked even if password is right 
#     print(f'Account Locked')
            
attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    password = input("Enter the password: ")
    
    if password == "admin123":
        print("Access Granted.")
        break
    else:
        print("Incorrect password.")

    print(f"Attempts left: {max_attempts - attempt}")
    attempt += 1

# if attempt > max_attempts:
else:               # better use else
    print("Account Locked")
