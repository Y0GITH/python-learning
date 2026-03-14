# guess the number within 3 given chance

# ok code 
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input(f'Guess the number : '))
#     guess_count += 1
#     if guess == secret_number:
#         print(f'you won!')
# the thing is, even if guesed it try one u still can try the second guess 

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input(f'Guess the number : '))
    guess_count += 1
    if guess == secret_number:
        print(f'you won!')
        break
else:
    print(f'sorry u failed.')