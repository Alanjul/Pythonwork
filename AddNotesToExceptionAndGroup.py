"""Enrich exceptions with notes
https://peps.python.org/pep-0678/#exception-handling"""
"""try:
    print(550/0)
except ZeroDivisionError as e:
    #call add notes to add more notes about the exception
    e.add_note("Denominator must be non-zero")
    raise e #raise the current exception"""

"""Exception handling groups and new version of exception called except*
https://peps.python.org/pep-0654/#exception-handling-groups
Enables the program to raise and handle multiple exception types simultaneously.
good for parallel and concurrent programming
where multiple tasks can raise exception and handled
simultaneously.

EXCEPTION GROUP contains multiple exception types"""
#ExceptionGroup Demo
#Demostrating raising and filtering exception group objects
from exceptiongroup import ExceptionGroup
def parallel_simulator():
    exceptions = [] #stores exceptions for Exception Group
    try:
        100/0
        #force zero divison exception
    except ZeroDivisionError as ex:
        #add notes for exception
        ex.add_note("Denominator must be non-zero")
        print(f' 1. {ex}')
        exceptions.append(ex) #appends the exception to exception group array
    try:
        int("Hello") #force value error
    except ValueError as va:
        va.add_note("Value must be an integer")
        print(f' 2. {va}')
        exceptions.append(va) #append to the array
    try:
        float("Emily")
    except ValueError as n:
        n.add_note("Value must be an float")
        print(f' 3. {n}')
        exceptions.append(n) #append to exception
    raise ExceptionGroup("Several exception have been raised", exceptions)
#main script
if __name__ == '__main__':
    print("Parallel simulator and exception handling group")
    try:
        parallel_simulator()
    except ExceptionGroup as ex:
        print(f' String representation of exception group\n{ex}')
        print("\nIndividual exception handling group")
        for e in ex.exceptions:
            #display the exception and their actual string name representation
            exception_type = type(e).__name__
            print(f" {exception_type}: {e}")
    print("\nuse except * to filter specific exception types")
    try:
        parallel_simulator()
        #helps to catch specific groups
    except* ValueError as value:
        value.add_note("Specific exception types are not allowed")
        print(f' caught error. {value}')
        for v in value.exceptions:
            exception_type = type(v).__name__
            print(f" {exception_type}: {v}")
            #filters exception related to zere division handling
    except* ZeroDivisionError as ex1:
        ex1.add_note("ZeroDivisionError")
        print(f' caught error. {ex1}')
        for v1 in ex1.exceptions:
            exception_type = type(v1).__name__
            print(f" {exception_type}: {v1}")


