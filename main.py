# bank_account.py

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient balance for withdrawal")
        else:
            print("Withdrawal amount must be positive")

    def apply_bank_fees(self):
        fee = self.balance * 0.05
        self.balance -= fee

    def display_account_details(self):
        return (
            f"Account Details:\n"
            f"Account Holder: {self.account_holder}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: {self.balance}\n"
        )


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0.0, interest_rate=0.02):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0.0, overdraft_limit=500):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
            else:
                print("Withdrawal exceeds overdraft limit")
        else:
            print("Withdrawal amount must be positive")
