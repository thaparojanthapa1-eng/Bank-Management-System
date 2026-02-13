class Bank:
    def __init__(self):
        self._customer_details = {}

    def get_customer_details(self):
        """Return all customer details."""
        return self._customer_details

    def add_customer_details(self, new_account_details):
        """Add or update customer details."""
        self._customer_details.update(new_account_details)

    def clear_customer_details(self):
        """Delete all customer details."""
        print("Deleting all customer details...")
        self._customer_details.clear()

    def find_account(self, customer_id):
        """Find a specific account by customer ID."""
        return self._customer_details.get(customer_id, "Account not found")

    def delete_account(self, customer_id):
        """Delete a specific account by customer ID."""
        if customer_id in self._customer_details:
            del self._customer_details[customer_id]
            print(f"Deleted account {customer_id}")
        else:
            print("Account not found")