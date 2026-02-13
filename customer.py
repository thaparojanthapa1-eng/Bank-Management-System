class Customer:
    def __init__(self, customer_id, customer_name, customer_login, password,
                 phone_no, email, address, citizenship_id, date_of_birth,
                 marital_status=None, occupation=None, income_level=None,
                 branch_id=None, nominee_name=None):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_login = customer_login
        self.password = password
        self.phone_no = phone_no
        self.email = email
        self.address = address
        self.citizenship_id = citizenship_id
        self.date_of_birth = date_of_birth
        self.marital_status = marital_status
        self.occupation = occupation
        self.income_level = income_level
        self.branch_id = branch_id
        self.nominee_name = nominee_name
        self.linked_accounts = []

    def add_account(self, account):
        self.linked_accounts.append(account)