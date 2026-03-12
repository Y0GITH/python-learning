# Ask user to enter numbers continuously.
#     Stop when user types "done"
#     Handle invalid input
#     Print total and average at the end
def analyze_numbers():
    numbers = []
    total = 0

    while True:
        user_input = input("Enter a number (or type 'done'): ")

        if user_input.lower() == "done":
            break

        try:
            num = float(user_input)   # convert safely
            numbers.append(num)
            total += num
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if len(numbers) == 0:
        print("No numbers entered.")
        return

    average = total / len(numbers)

    print("\nTotal:", total)
    print("Average:", average)
    
analyze_numbers()
