from bank import Bank
from account import Account
from customer import Customer

def main():
    bank = Bank()
    print("====Welcome To Rojan Bank Limited====")

    while True:
        print("\nEnter 'new' to create a new account")
        print("Enter your Customer ID to log in")
        print("Enter 'exit' to quit")
        customer_id = input("Customer ID: ").strip()

        if customer_id.lower() == "exit":
            print("Thanks for using our services!")
            break

        if customer_id.lower() == "new":
            customer_id = input("Set a unique Customer ID: ").strip()
            if bank.find_account(customer_id) != "Account not found":
                print("Customer ID already exists. Try logging in.")
                continue

            name = input("Enter your full name: ").strip()
            login = input("Choose a login username: ").strip()
            password = input("Set a password: ").strip()

            new_customer = Customer(customer_id, name, login, password)
            new_account = Account(customer_id, balance=0)
            bank.add_customer_details({customer_id: {"customer": new_customer, "account": new_account}})
            print(f"Customer {customer_id} created successfully!")
            continue

        customer_data = bank.find_account(customer_id)
        if customer_data == "Account not found":
            print("Customer ID does not exist")
            continue

        customer = customer_data["customer"]
        account = customer_data["account"]
        print(f"\nWelcome, {customer.customer_name}")

        while True:
            print("\nSelect an option:")
            print("1. Check balance")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Logout")

            choice = input("Enter option number: ").strip()

            if choice == "1":
                print(f"Your balance: {account.balance_check()}")

            elif choice == "2":
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print(f"Deposited {amount} successfully")
                except ValueError:
                    print("Invalid amount")

            elif choice == "3":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdrawal(amount)
                    print(f"Withdrawal of {amount} processed")
                except ValueError:
                    print("Invalid amount")

            elif choice == "4":
                print(f"Logging out {customer.customer_name}...\n")
                break

            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    main()