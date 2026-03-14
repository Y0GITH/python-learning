class Transaction:
    def __init__(self , id , status , amount ):
        self.id = id
        self.status = status
        self.amount = amount

    def check(self):
        if 'SUCCESS' in self.status:
            return 'GOOD'
        else:
            return 'INCOMPLITE'

a = Transaction('ABC123' , 'SUCCESS' , 1000)
print(a.check())    