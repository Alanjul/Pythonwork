#base class    subclasesss
#student       graduateStudent, underGraduate
#shape         circle, Triangle, Rectangle, Sphere, cube
#Loan          carLoan, HomeImprovementLoan, MortgageLoan
#Employee      Faculty, Staff
#BankAccount    checkingAccounts, SavingAccount
#base class(CommunityMember)  subclass Employee, student, alum
from decimal import Decimal

from jedi.parser_utils import for_stmt_defines_one_name

from StringConcatenation import firstName


class commissionEmployee:
    """An employee who gets paid commission based on gross sales"""
    def __init__(self, first_name, last_name, sss, rate, sales):
        self._first_name = first_name
        self._last_name = last_name
        self._sss = sss

        self._sales = sales
        self ._rate = rate
    @property
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name
    @property
    def sss(self):
        return self._sss
    @property
    def rate(self):
        return self._rate
    @property
    def sales(self):
        return self._sales
    @rate.setter
    def rate(self, rate):
        #ensuring rate is decimal
        #if isinstance(rate, Decimal):
            #rate_value = rate
        #else:
            #rate_value = Decimal(rate)
        if not(Decimal('0.00') < rate < Decimal('1.0')):
            raise ValueError('Rate must be between 0.0 and 1.0')
        self._rate = rate
    @sales.setter
    def sales(self, sales):
        if sales < Decimal('0.00'):
            raise ValueError('Sales must be greater than 0.0')
        self._sales = sales
    def earning(self):
        #Calcuate the earnings
        return self.sales * self.rate
    def __repr__(self):
        #return the string representation of rep
        return (f'commission employee: first_name: {self._first_name},'
                f' last_name: {self._last_name}, \n'
                f'social Security number: {self._sss} sales: {self.sales:.2f} '
                f'commission: {self.rate:.2f}')

