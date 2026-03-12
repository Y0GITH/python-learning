# start and spot the car

# good but not good enough for too logic
# command = ""
# while True: # code run till break is executed, as its true
#     command = input(f'>>').lower()
#     if command == "start":
#         print(f'car started...')
#     elif command == "stop":
#         print(f'car stopped.')
#     elif command == "help":
#         print(f"""
# start - to start the car 
# stop  - to stop the car 
# quit  - to exit                             
#               """)
#     elif command == "quit":
#         break
#     else:
#         print(f'sorry, i dont understand that!')
# as we can run start twice, as it dosent make sence as car is already started 
command = ""
started = False
while True: # code run till break is executed, as its true
    command = input(f'>>').lower()
    if command == "start":
        if started :
            print(f'car is already started!')
        else:   
            started = True    
            print(f'car started...')
    elif command == "stop":
        if not started:
            print(f'car is already stopped!')
        else:
            started = False    
            print(f'car stopped.')
    elif command == "help":
        print(f"""
start - to start the car 
stop  - to stop the car 
quit  - to exit                             
              """)
    elif command == "quit":
        break
    else:
        print(f'sorry, i dont understand that!')
# now we can't start or stop car twice        
