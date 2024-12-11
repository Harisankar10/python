class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0.0):
        """Constructor to initialize the bank account with provided details."""
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        """Method to deposit money into the bank account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance to withdraw the requested amount.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Account Type: {self.account_type}, Balance: {self.balance}"

account1 = BankAccount(account_number="10010505494", name="batman", account_type="savings", balance=1000000000000)
account2 = BankAccount(account_number="10024654446", name="superman", account_type="Savings", balance=2000)


print(account1)
print(account2)


account1.deposit(50000)
account1.withdraw(200000)
account1.withdraw(1500)
print(f"Final balance of account1: {account1.get_balance()}")
print(f"Final balance of account2: {account2.get_balance()}")
