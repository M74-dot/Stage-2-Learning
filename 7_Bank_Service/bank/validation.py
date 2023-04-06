import re


def validate_account_name(account_name):
    if len(account_name) < 3:
        print('Invalid account name. Account name should contain at least 3 characters')
        return False
    else:
        return True
    

def validate_account_number(account_number):
    regex = "^[0-9]{9}$"
    if not re.match(regex,account_number):
        print('Invalid account number. Account number should contain 11 digits')
        return False
    else:
        return True
    

def validate_amount(amount):
    if not amount.isdigit():
        print('Invalid amount.')
        return False
    else:
        return True
    