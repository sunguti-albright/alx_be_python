# bank_account.py

class BankAccount():
    def __init__(self, initial_balance = 0):
        self.__account_balance = initial_balance
        
    def deposit(self, amount):
        self.__account_balance += amount
        
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
    def display_balance(self):
        print(f"The Current Balance is : ${self.__account_balance:.2f}")
        
