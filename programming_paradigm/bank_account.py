class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with optional starting balance (default=0)."""
        self.__account_balance = initial_balance   # Encapsulated attribute

    def deposit(self, amount):
        """Add money to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient, else return False."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print current balance in user-friendly format."""
        print(f"Current Balance: ${self.__account_balance}")
