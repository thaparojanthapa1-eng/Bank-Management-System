class Bank:
    def __init__(self):
        self._customer_details = {}

    @property
    def customer_details(self):
        return self._customer_details

    @customer_details.setter
    def customer_details(self, new_account_details):
        self._customer_details.update(new_account_details)

    @customer_details.deleter
    def customer_details(self):
        print("Deleting all customer details...")
        self._customer_details.clear()

    def find_account(self, customer_id):
        return self._customer_details.get(customer_id, "Account not found")

    def delete_account(self, customer_id):
        if customer_id in self._customer_details:
            del self._customer_details[customer_id]
            print(f"Deleted account {customer_id}")
        else:
            print("Account not found")