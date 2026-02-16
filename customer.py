class Customer:
    def __init__(self, customer_id, customer_name, customer_login, password,
                 phone_no, email, address, citizenship_id, date_of_birth,
                 marital_status=None, occupation=None, income_level=None,
                 branch_id=None, nominee_name=None):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_login = customer_login
        self.password = password