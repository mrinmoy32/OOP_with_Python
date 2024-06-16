class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit funds into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw funds from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        """Get the current account balance."""
        return self.balance

# Example usage:
account1 = BankAccount(account_number="123456", initial_balance=1000)
print(f"Account balance: ${account1.get_balance()}")
account1.deposit(200)
account1.withdraw(150)
print(f"Account balance: ${account1.get_balance()}")
