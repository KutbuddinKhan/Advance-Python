# Static methods
class Payment:
    initial_balance = 1000

    def __init__(self, recipient,  amount):
        self.recipient = recipient
        self.amount = amount

    def check_balance(self):
        return Payment.initial_balance - self.amount
    
    @classmethod
    def update_initial_balance(cls, new_balance):
        cls.initial_balance = new_balance

    @staticmethod
    def check_valid_transaction(hour):
        if hour >= 8 and hour <= 17:
            return True
        else:
            return False

        

transaction1 = Payment("A", 25)
print(transaction1.check_valid_transaction(7))