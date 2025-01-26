import numpy as np
from decimal import Decimal
answer =f'{15.489:.2f}' #format to 2 decimal places
print(answer)
answer1 = f'{10:d}' #format as integers
print(answer1)
answer2 = f'{65:c} {97:c}' # format them as a character
print(answer2)
answer3 = f"{"hello":s} {7}" # format as astring
print(answer3)
answer4 = f"{Decimal('10000000000000.0'):.3f}"  #convert it to decimal values
print(answer4)
answer5 = f"{Decimal('100000000000.0'):.3e}"  #exponential notation
print(answer5)
answer6 = f"{Decimal('100000000000.0'):.3E}"  #exponetial function
characterCode = f"{58:c}, {45:c}, and {41:c}" #displaying character codes
print(characterCode)

#using field wuth and alignment
rightAlign = f'[{27:10d}' #right alignment
print(rightAlign)
#formating floats
rightAlign2 = f'{3.5:10f} ' #rightft alignment with 6 trailing zeros
print(rightAlign2)
stringAlign = f'[{"hello" :10}]' #strings are left aligned automatically
print(stringAlign)

#format in left alignment
leftAlignment = f"[{27.12:<10f}]"
print(leftAlignment)
#center the value
centerAlignment = f"[{45:^10d}]"
print(centerAlignment)
leftAlignment2 = f"[{45:<10d}]"
print(leftAlignment2)
name = "AMANDA"
print(f"[{name:10s}]") #left aligned
print(f"[{name:>10s}]") #right aligned
print(f"[{name:^10s}]")  #center aligned