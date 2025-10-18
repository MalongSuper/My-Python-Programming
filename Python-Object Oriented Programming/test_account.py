# Class Test Account

class Account:
    def __init__(self, number=0.0, balance=0.0, account_type=""):
        print("Account Created")
        self.number = number
        self.balance = balance
        self.account_type = account_type

    def get_number(self):
        return self.number

    def get_balance(self):
        return self.balance

    def get_type(self):
        return self.account_type

    def to_string(self):  # Display the information as String
        print(f"Account[Number = {str(self.number)}, Balance = {str(self.balance)}, "
              f"AccountType = {self.account_type}]")

    def credit(self, amount):  # Add amount to balance
        self.balance = self.balance + amount

    def debit(self, amount):  # Subtract amount to balance
        if self.balance < amount:
            raise ValueError("Cannot subtract the balance to the given amount, "
                             "or Amount Exceeded")
        self.balance = self.balance - amount

    def transfer_to(self, amount, to_account):
        if self.balance < amount:
            raise ValueError("Cannot transfer the given amount from the balance, "
                             "or Amount Exceeded")
        # Transfer from Account to Account
        self.balance = self.balance - amount
        to_account.balance = to_account.balance + amount


def main():
    account1 = Account(11, 1000, "USD")
    account2 = Account(12, 1000, "USD")
    # Add 100$ to account1, and 50$ to account2
    account1.credit(100)
    account2.debit(50)
    account1.transfer_to(70, account2)
    print("=================Account1=================")
    print(f"+ Number: {account1.get_number()}")
    print(f"+ Balance: {account1.get_balance()}")
    print(f"+ Account Type: {account1.get_type()}")
    print("==========================================")
    print()
    print("=================Account2=================")
    print(f"+ Number: {account2.get_number()}")
    print(f"+ Balance: {account2.get_balance()}")
    print(f"+ Account Type: {account2.get_type()}")
    print("==========================================")


main()
