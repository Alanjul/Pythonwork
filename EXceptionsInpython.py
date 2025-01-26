#sample exception handling example
while True:
    #attemot to convert and divide values
    try:
        number = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        result = number / number2
    except ValueError: #trying to convert non-numeric to int
        print("Invalid input, please enter a valid integer")
    except ZeroDivisionError: #division by erro
        print("Invalid input, you entered 0, we can't divide by zero")
    else: #no exception occurs
        print(f"The number {number}/ {number2} is {result:.2f}")
        break  #terminate the loop
def try_it(value):
    try:
        x = int(value)
    except ValueError:
        print("Invalid input, Value can't be converted")
    else:
        print(f"The number {value} is {x}")
def try_another(value):
    try:
        x = int(value)
    except ValueError:
        print(f"Invalid input, {value} can't be converted")
    else:
        print(f"The number {value} is {x}")
print(try_it(10.7))
print(try_another("hello"))

try:
    print("Try suite with no exceptions raised")
except:
    print("not executes because no exceptions raised")
else:
    print("No exceptions raised in try suite")
finally:
    print("it is always executed")
try:
    print("Try suite with no exceptions raised")
    int("hello")
except ValueError:
    print("ValueError raised in try suite")
else:
    print("No exceptions raised in try suite")
finally:
    print("finally  is always executed")
try:
    with open("gradez.txt", mode='r') as gradez_file:
        print(f"{"ID":<3} {"Name":<10}{"Grades"}")
        for grade in gradez_file:
            ID, name, grades = grade.split('')
            print('f{ID:<3}{name:<10}{grades}')

except FileNotFoundError:
    print("File not found")
'''Raise Exception  
To explicitly raise an exception 
we use raise ExceptionClassName
Creates an object of the specified exception class
Class name may be followed by parentheses containing arguments to
initialize the exception object
Code that raises an exception first should release any resource acquired before the exception
occurred 
python's built-in exception types  https://docs.python.org/3/library/exceptions.html''
'''
print("Stack trace and unwinding the stack trace")
def function1():
    function2()
def function2():
    raise Exception("An exception has occurred")
print(function1())

