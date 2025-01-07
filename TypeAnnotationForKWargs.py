"""pep 692  using typeDict for more precise **kwargs typing
https://peps.python.org/pep-0692/#type-annotation-for-keyword-arguments
function's **kwargs can be passed as any arbitrary number of keyword arguments
or dictionary preceded by ** unpacking operators to pass a dictionary's
keys-value pairs a keywrod argument
TYPEDICT subclass can document keywords arguments names and their types
Each keyword argument name is the attribute and corresponding value's type is
 type hint
"""
from typing import  TypedDict, Tuple

from NewFunctions import average


#class student inherits from typeDict
class Student(TypedDict):
    name: str #string name
    grade: list[int] #passed as list of integers
#function calculateGpa uses Student as type hint
#receives an arbitrary number of keyword arguments and types specified by student
def calculategrade(**kwargs: Student) -> Tuple[str,float]:
    #getname or return name not specified
    names = kwargs.get('name', 'Name not specified')
    #return grade or empty list
    grade = kwargs.get('grade', [])
    average_grade = sum(grade) / len(grade) if grade else 0.0
    return names, average_grade
#students dictionary that adheres to Student
students: Student = {"name": "Daniel", "grade": [100, 95, 93]}

#function CalculateGrade receives kwargs arguments
name, grade_average = calculategrade(**students)
print(f"{name}'s average grade: {grade_average}")

