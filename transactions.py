from datetime import datetime

class Transactions:
    def __init__(self, customer_id, transaction_amount, transaction_type):
        self.customer_id=customer_id
        self.transaction_amount=transaction_amount
        allowed_transaction_types=["Withdrawal", "Deposit"]
        if transaction_type in allowed_transaction_types:
            self.transaction_type=transaction_type
        else:
            print(f"Select a valid transaction type:    {allowed_transaction_types}")