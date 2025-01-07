"""https://peps.python.org/pep-0709/0t-of-lists-of-lists
for eacj comprehesnion, the interpreter transformed int into function
called that function to perform task
inline eliminates overhead of creating and calling function
to improve performance of function
"""

"""Zip  for optional length checking
https://peps.python.org/pep-0618/
Sometimes zip arguments of different lengths should be a logic error
if so, pass strict=True as zip's lasr argument
value error occurs if arguments don't have same length"""
names = ["Alan","Emily", "Josephine", "paul"]
grade_point = [3.5, 4.0, 3.75]
try:
    for name, grade in zip(names, grade_point, strict=True): #error will be produced
        print(f"{name = } is {grade = }.")
except ValueError as e:
    print("The lists have different lengths.")
    print(f"Details:{e}")


for name, gpa in zip(names, grade_point):  #no error will be produced shortest evaluated
    print(f"{name = } is {gpa = }.")

#dictionary operators
"""Pep 584; adds union operator to dict
https://peps.python.org/pep-0584/0t-of-lists-of-lists
it is possible to merge union operators | and |= """
city1 = {"New York": "Buffalo", "Kansas": "Topeka"}
city2 = {"California": "San Jose", "Missouri": "Jefferson"}
print(city1 |city2) #merge them to gether to create a new merged dictionary
city1 |= city2
print(city1)  #modifies values in cities,duplicates will be removed
