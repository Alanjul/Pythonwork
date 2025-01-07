"""Structural pattern matching: specification
https://peps.python.org/pep-0634/#structural-pattern-matching
specify guard conditions that help determine where there's a match
Function calcualte receives an arbitary list of arguments representing various arithmetic
operations and numeric operands
*args gethers argument's values into a tuple
"""
from unittest import case


def calculate(*args):
    match args: #list of arguments
        case [value]: #no operation specified; just return value
            return value
        case [op, value] if op in ('+', '-'):#unary operator
             return value if op == '+' else -value
        case [value1, '+', value2, '+', value3]: #addition operators
            return value1 + value2 + value3
        case[ value1 , '-', value2]:  #subtraction operator
            return value1 - value2
        case [value1, '*', value2, '*', value3]: #multiplication operator
            return value1 * value2 * value3
        case [value1, '/', value2]: #divide operator
            return value1 / value2
        case [value1, '%', value2]: #modulus operator
            return value1 % value2
        case [value1, '^', value2]:  #exponentiation operator **
            return value1 ** value2
        case [value1, '<', value2]:  #less than
                return value1 < value2
        case [value1, '>', value2]:  #greater than
            return value1 > value2
        case _: #default case that matches any pattern
            return None
number1 = [67,78,41]
number2 = [69,88,41]
#answer = calculate(number1,'-', number2) #error will be produced

answer2 = calculate(10, "+", 3, '+', 12)
print(answer2)
answer = calculate(10, "*", 3, '*', 12)
answer3 = calculate(10, "-", 3,)
print(answer3)
if calculate(10, "+", 3, '+') == None: #error : missing right operand
    print("Error, calculate failed")
"""Positional only parameters
python positional only parameters 
https://peps.python.org/pep-0570/#position-only-parameters"""
def average(number1, number2, number3):
    return (number1 + number2 + number3)/3
print(average(7,20,15)) #call with positional arguments
#using keywords arguments
average(number3 =20, number1 = 7,number2=18)  