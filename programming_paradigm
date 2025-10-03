# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional starting balance (default = 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a given amount into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw a given amount if funds are sufficient.
        Returns True if successful, otherwise False.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance formatted with two decimal places."""
        print(f"Current Balance: ${self.account_balance:.2f}")
