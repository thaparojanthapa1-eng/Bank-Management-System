class Account:
    def __init__(self, customer_id, balance):
        self.customer_id=customer_id
        self.balance=balance

    def balance_check(self):
        return self.balance

    def deposit(self, amount):
        self.balance+=amount

    def withdrawal(self, amount):
        if self.balance<amount:
            print("Insufficient balance")
        else:
            self.balance-=amount