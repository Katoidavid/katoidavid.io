from main import BankAccount, SavingsAccount, CheckingAccount


# Create an instance of SavingsAccount
savings = SavingsAccount("Antony Katpoi", "123456789", balance=1000)
savings.deposit(200)
savings.apply_interest()
savings.apply_bank_fees()

# Display details of SavingsAccount
print(savings.display_account_details())

# Create an instance of CheckingAccount
checking = CheckingAccount("Antony Katpoi", "987654321", balance=500)
checking.deposit(300)
checking.withdraw(1000)  # Testing overdraft limit
checking.apply_bank_fees()

# Display details of CheckingAccount
print(checking.display_account_details())
