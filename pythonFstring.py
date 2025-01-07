"""
F-strings in the grammar
"""
print("F-string in python")
#interpreter will recorgnizes quotes in place holder as strirng literal being formated
#not delimiters for f string
print(f'Face{'Frequency': >13}')
#macth -case used as if else in python and similar to switch
#expression after is the subject expression
grade = "C"
match grade:
    case "A":
        print("A")
    case "B":
        print("B")
    case "C":
        print("C")
    case "D":
        print("D")
    case "F":
        print("F")

    case _: #irrefutabe case block similar to default in other programming languages
        print("Invalid grade entered")
#assignment expression
grades = int(input("Enter the grades (0 - 100: "))
if grades >= 67:
    print(f"{grades} is the passing grade")
else:
    print(f"{grades} is not the passing grade")
#using assigment operators
if (grades:= int(input("Enter the grades (0 - 100): "))) >= 67:
    print(f"{grades} is the passing grade")
else:
    print(f"{grades} is not the passing grade")
    #walrus operator  is good for regular expressions and sentinel -controlled loop
    #conditions
    #if clause of compression

"""Statistics model like Function mode update, Function multimode
mode:
https://docs.python.org/3/library/statistics.html#statistics.mode
multimode
https://docs.python.org/3/library/statistics.html#statistics.multimode
when a dataset has two or more frequent model values it is called a multi-modal"""
import statistics
grades2 = [85,93,45,89,85,93]
print(statistics.mode(grades2))
print(statistics.multimode(grades2))