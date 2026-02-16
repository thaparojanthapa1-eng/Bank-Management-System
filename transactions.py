from datetime import datetime

class Transactions:
    def __init__(self, customer_id, transaction_amount, transaction_type):
        self.customer_id=customer_id
        self.transaction_amount=transaction_amount