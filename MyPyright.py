
"""Static code analysis tool like pyright(https://github.com/microsoft/pyright
mypy (https://mypy-lang.org/) checks type hints """
from collections import defaultdict
from typing import TypedDict, Tuple,List,Dict, ClassVar
class Student(TypedDict):
    name: str #string name
    grade: list[int] #passed as list of integers
#function calculateGpa uses Student as type hint
#receives an arbitrary number of keyword arguments and types specified by student
"""def calculategrade(**kwargs: Student) -> Tuple[str,float]:
    #getname or return name not specified
    names = kwargs.get('name', 'Name not specified')
    #return grade or empty list
    grade = kwargs.get('grade', [])
    average_grade = sum(grade) / len(grade) if grade else 0.0
    return names, average_grade
#students dictionary that adheres to Student
students: Student = {"name": 100, "grade": ['A', 'B-', 'A-']}

#function CalculateGrade receives kwargs arguments
name, grade_average = calculategrade(name=students['name'], grade=students['grade'])
print(f"{name}'s average grade: {grade_average}")"""
#type union operator for type hints
"""type union operator PEP 604 https://peps.python.org/pep-0604 
enables x|y can return either type x or y"""
def square(number: int | float) -> int|float:
    return number * number
print(square(3.5))

"""Built in collection types in type hint
type hinting to help in generating code
pep585 https://peps.python.org/pep-0585
e.g"""
faces :ClassVar[list[int]]

