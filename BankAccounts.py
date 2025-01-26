#class Accounts definitions
from decimal import Decimal
class Account:
    #constructor
    def __init__(self, name, balance):
        #initialize account name and balance
        self.name = name
        if (balance >0.0):
            self.balance = balance
        else:
            raise ValueError("Balance cannot be negative")

    def deposit(self, amount):
        #deposit money to account
        if amount < Decimal("0.0"):
            raise ValueError("Deposited amount cannot be negative")
        else:
            self.balance += amount
    def withdraw(self, amount):
        #withdraw money from the account
        if (amount > self.balance):
            raise ValueError("Withdrawal amount cannot be greater than balance")

        elif(amount < Decimal("0.0")):
            raise ValueError(" withdraw amount cannot be negative")

        self.balance -= amount

