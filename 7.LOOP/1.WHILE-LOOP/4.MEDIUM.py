# A user must enter marks between 0 and 100.
# Use a while loop to keep asking until a valid mark is entered.
while True:
    marks = int(input("Enter marks: "))
    if 0 <= marks <= 100:
        print("Valid marks!")
        break
    print("Invalid mark. Must be between 0-100.")
