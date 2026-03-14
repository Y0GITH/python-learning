#Create a class BankAccount
#    attributes: name, balance
#    methods:
#    deposit(amount)
#    withdraw(amount)
#    show_balance()
#    prevent overdraft
class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Withdrawal denied.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        return print(f"Current Balance: {self.balance}")

account1 = BankAccount("Yogith", 5000)

account1.show_balance()
account1.deposit(2000)
account1.withdraw(1000)
account1.withdraw(10000)  
account1.show_balance()
