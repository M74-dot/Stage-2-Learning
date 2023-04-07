class Account:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposite(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False
        else:
            self.balance += amount
            print(
                f"{amount} deposited to your account."
                " Available balance is INR {self.balance}"
            )
            return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False
        elif self.balance < amount:
            print("Insufficient balance")
            return False
        else:
            self.balance -= amount
            print(
                f"{amount} withdrawn from your account."
                " Available balance is INR {self.balance}"
            )
            return True
