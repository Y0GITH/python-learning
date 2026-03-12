class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def is_success(self):
        if self.status.upper() == "SUCCESS":
            return "Transaction Completed"
        else:
            return "Transaction Failed"

class InternationalTransaction(Transaction):
    def __init__(self, txn_id, amount, status, currency, exchange_rate):
        super().__init__(txn_id, amount, status)
        self.currency = currency
        self.exchange_rate = exchange_rate

    def convert_to_inr(self):
        return self.amount * self.exchange_rate

    def show_transaction(self):
        print(f"Transaction ID : {self.txn_id}")
        print(f"Status         : {self.is_success()}")
        print(f"Amount         : {self.amount} {self.currency}")
        print(f"INR Value      : ₹{self.convert_to_inr()}")

txn_id = input("Enter Transaction ID: ")
amount = float(input("Enter Amount: "))
status = input("Enter Status (SUCCESS / FAILED): ")
currency = input("Enter Currency (e.g., USD, EUR): ")
exchange_rate = float(input("Enter Exchange Rate to INR: "))
txn = InternationalTransaction(
    txn_id,
    amount,
    status,
    currency,
    exchange_rate
)
txn.show_transaction()
