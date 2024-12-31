from decimal import Decimal
class AccountTest:
    """Account class test to demostrate doctest"""
    def __init__(self,name, balance):
        """
        Initializing an account oject

        >>> account1 = AccountTest("John", Decimal("20.00"))
        >>> account1.name
        'John'
        >>> account1.balance
        Decimal('20.00')

        >>> account2 = AccountTest("John Adama", Decimal("-20.00"))
        Traceback (most recent call last):
        ...
        ValueError: Insufficient balance, balance can't be negative

        >>> account1.deposit(Decimal("50.00"))
        >>> account1.balance
        Decimal('70.00')

        account1.deposit(Decimal("-50.00"))
        Traceback (most recent call last):
        ...
        ValueError: Insufficient money, amount can't be negative'
        """
        if balance < Decimal("0.00"):
            raise ValueError("Insufficient balance, balance can't be negative")
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        """Deposit an amount of money"""
        if amount < Decimal("0.00"):
            raise ValueError("Insufficient money, amount can't be negative")
        self.balance += amount
    def withdraw(self, amount):
        """Withdraw an amount of money"""
        if amount > self.balance:
            raise ValueError("Insufficient balance, amount can't be greater than balance")
        self.balance -= amount
    if __name__ == "__main__":
        import doctest
        #create the test results for us
        doctest.testmod(verbose=True)

