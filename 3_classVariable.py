# Class Variables
class Payment:
    initial_balance = 1000

    def __init__(self, recipient,  amount):
        self.recipient = recipient
        self.amount = amount

    def check_balance(self):
        return Payment.initial_balance - self.amount
        


payment1 = Payment("A", 25) 
print(payment1.check_balance())