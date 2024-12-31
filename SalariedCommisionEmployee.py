from Commission import commissionEmployee
from decimal import Decimal

class salariedCommisionEmployee(commissionEmployee):
    """An employee who gets paid salary plus comission"""
    def __init__(self, first_name, last_name, sss, rate, sales, salary):
        #initializing salalaried employee attributes
        super().__init__(first_name, last_name, sss, rate, sales) #inherited from the base class
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, salary):
        if salary < Decimal('0.00'):
            raise ValueError('Salary cannot be less than 0.00')
        self._salary = salary
    #calculate earning
    def earning(self):
        return super().earning() + self._salary
    def __repr__(self):
        #return string representation of repr()
        return 'Salaried' + super().__repr__() + f'(base salary {self.salary:.2f})'
s = salariedCommisionEmployee('Bob', 'lewis',
                              '444-41-4532', Decimal('50000.00'), Decimal('0.6'),
                              Decimal('300.00'))
c = commissionEmployee('James', 'john',
                       '441-44-5555', Decimal('0.5'), Decimal('300'))
print(f'{s.earning():,.2f} ')
#checking if salariedCommissionEmpoyee is a subclass of CommissionEmpyoee
print(issubclass(salariedCommisionEmployee,commissionEmployee))
#checking is isinstance  where object is the first argument and class is the second argument
print(isinstance(s, salariedCommisionEmployee))
print(isinstance(s, commissionEmployee))
print(isinstance(c, salariedCommisionEmployee)) #prints false
#polymorphic processing woth a for loop
employees = [c,s]
for employee in employees:
    print(employee)
    print(f'{employee.earning():,.2f}')