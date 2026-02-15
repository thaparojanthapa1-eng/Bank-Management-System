from bank import Bank
from account import Account
from transactions import Transactions
from customer import Customer

def main():
    create_new=""
    bank=Bank()

    print("====Welcome To Rojan Bank Limited====")
    print("Enter Customer id to continue")
    print("Enter exit to EXIT")
    print("Enter new to create new account")

    while True:
        Customer_id=input("\nEnter your customer id:   \n")

        if Customer_id.lower().strip()=="exit":
            print("....Thanks for using our services....")
            break

        customer=bank.find_account(Customer_id)
        if customer=="Account not found" and Customer_id!="new":
            print("\nCustomer_id doesn't exist")  
            print("\nWould you like to create a new account to use our services?")
            if Customer_id!="new":
                create_new = input("Enter 'new' to create new account: ").strip().lower()
            else:
                create_new="new"
        if create_new == "new" or Customer_id.lower().strip()=="new":
            name = input("Enter your full name: ").strip()
            login = input("Choose a login username: ").strip()
            password = input("Set a password: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone number: ").strip()
            address = input("Address: ").strip()
            citizenship = input("Citizenship ID: ").strip()
            dob = input("Date of Birth (YYYY-MM-DD): ").strip()
            marital_status = input("Marital Status (optional): ").strip() or None
            occupation = input("Occupation (optional): ").strip() or None
            income_level = input("Income Level (optional): ").strip() or None
            nominee_name = input("Nominee Name (optional): ").strip() or None
            linked_account_list=[]
        
            new_account=Account(Customer_id, balance=0)
            print("\nDoes a user have an already existing bank account to link to:  ")
            account_link=input("\nEnter 'Yes' if you have a pre-existing account and 'No' if you don't have a pre-existing account:   ").lower().strip()
            if account_link=="yes":
                while True:
                    linked_account=input("Enter customer_id of the account you want to link with:  ")
                    linked_account_check=bank.find_account(linked_account)
                    if linked_account_check=="Account not found":
                        print("The account doesn't exist.\nPlease try again")
                        retry=input("Enter Yes to retry and No to skip linking account").lower().strip()
                        if retry!="yes":
                            print("Skipping account linking.")
                            break
                    else:
                        linked_account_list.append(linked_account_check)
                        print(f"Your account {new_account.customer_id} has been successfully linked to {linked_account}")

            new_customer = Customer(
                customer_id=Customer_id,
                customer_name=name,
                customer_login=login,
                password=password,
                phone_no=phone,
                email=email,
                address=address,
                citizenship_id=citizenship,
                date_of_birth=dob,
                marital_status=marital_status,
                occupation=occupation,
                income_level=income_level,
                nominee_name=nominee_name,
                linked_accounts=linked_account_list
            )   
            customer=new_customer         
            bank.add_customer_details({Customer_id: new_customer})
            print(f"Customer {Customer_id} created successfully!\n")
            
            print(f"Welcome, {customer.customer_name}")
            services_check=input("Do you want to use our services?\nPress Yes to continue and anything else to exit").lower().strip()
            if services_check!="yes":
                break
            else:
                while True:
                    print("\nSelect an option:")
                    print("1. Check balance")
                    print("2. Deposit money")
                    print("3. Withdraw money")
                    print("4. View linked accounts")
                    print("5. Logout")
                    choice = input("Enter option number: ").strip()
                    acc=Account(customer.customer_id, balance=0)

                    if choice=="1":
                        print(f"The balance is {acc.balance_check}")

                    if choice=="2":
                        amount = float(input("Enter amount to deposit: "))
                        print(acc.deposit(amount))

                    if choice=="3":
                        amount = float(input("Enter amount to withdraw: "))
                        print(acc.withdrawal(amount))

                    if choice=="4":
                        print("Linked accounts:")
                        for linked_acc in customer.linked_accounts:
                            print(f"Linked Account: {linked_acc}")

                    elif choice == "5":
                        print(f"Logging out {customer.customer_name}...\n")
                        break

                    else:
                        print("Invalid option. Try again.")

if __name__=="__main__":
    main()