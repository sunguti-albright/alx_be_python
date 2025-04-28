# bank_account.py

class BankAccount:
    """A simple BankAccount class with deposit, withdraw, and display balance methods."""

    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add amount to account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds are available."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
