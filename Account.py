from decimal import Decimal
from BankAccounts import Account

account1 = Account('John Green', Decimal('1000.00')) #constructor account class
print(account1.balance)
#print(account1.deposit(Decimal('-1000.00')))
account1.withdraw(Decimal('200.00'))
print(account1.balance)
#print(account1.withdraw(Decimal('-1000.00')))
account1.balance = (Decimal('-200.00'))
print(account1.balance)