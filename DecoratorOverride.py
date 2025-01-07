from functools import wraps
from decimal import Decimal
from typing import override
class commisionEmployee:
    """Employee class demostrating commission employee who get paid based on
    gross sales"""
    def __init__(self,name:str,rate:Decimal, sales: Decimal):
        #initializing the attributes
        self._name = name
        self._rate = rate
        self._sales = sales
    @property
    def name(self):
        return self._name
    @property
    def rate(self):
        return self._rate
    @property
    def sales(self):
        return self._sales
    @sales.setter
    def sales(self, sales:Decimal):
        if sales < Decimal('0.00'):
            raise ValueError('sales must be greater than or equal to 0.00')
        self._sales = sales
    @rate.setter
    def rate(self, rate:Decimal):
        if rate < Decimal('0.00'):
            raise ValueError('rate must be greater than or equal to 0.00')
        self._rate = rate

    def earning(self):
        #returns earnings
        return self.sales * self.rate
          
