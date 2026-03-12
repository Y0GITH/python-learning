# Keep asking the user to enter a number until they enter 0, then stop.
a = -1  # start with any number except 0
while True:
    a = int(input("Guess the number between 0–5: "))
    if a == 0:
        print("You guessed it right! :-)")
        break
    else:
        print("Wrong guess, try again! :-)")
