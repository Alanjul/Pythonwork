"""Duck Typing is a programming style which doesn't
look at an object's type to determine the right interface. Instead, the method
or attribute is simply called or used
https://docs.python.org/3/glossary.html#term-duck_typing"""
from decimal import Decimal
from Commission import commissionEmployee
from SalariedCommisionEmployee import salariedCommisionEmployee

class WellPaidDuck:
    def __repr__(self):
        return "I am well paid duck"
    def earning(self):
        return Decimal("1_000_000.00")
c = commissionEmployee("John", "Hakiza",'331-11-1123',
                       Decimal('0.61'), Decimal("10000.00"))
s = salariedCommisionEmployee("Peter", "Hakiza",'441-44-5542',Decimal("0.05"),
                              Decimal("1000.00"), Decimal("5000"))
d = WellPaidDuck()
employees = [c,s,d] #list created for the instance variables
for employee in employees:
    print(f"The amount of is {employee.earning():,.2f}")