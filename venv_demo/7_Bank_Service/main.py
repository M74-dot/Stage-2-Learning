from bank.account import Account
from bank.validation import (
    validate_account_name,
    validate_account_number,
    validate_amount,
)


def main():
    account_number = input("Enter your account number: ")
    if not validate_account_number(account_number):
        return

    account_name = input("Enter your account name: ")
    if not validate_account_name(account_name):
        return

    amount = input("Enter account balance: ")
    if not validate_amount(amount):
        return

    # create an Account object
    manisha = Account(account_number, account_name, int(amount))

    while True:
        print("\n choose option: ")
        print("1. Deposite")
        print("2. Withdraw")
        print("3. Exit")

        option = int(input("Enter your choice: "))

        if option == 1:
            amount = input("Enter the amount to be deposite: ")
            if not validate_amount(amount):
                continue
            manisha.deposite(int(amount))

        elif option == 2:
            amount = input("Enter the amount to be withdraw: ")
            if not validate_amount(amount):
                continue
            manisha.withdraw(int(amount))

        elif option == 3:
            print("Exiting..")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
