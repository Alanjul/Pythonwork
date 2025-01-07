"""Enums support for enumerations
https://docs.python.org/3/library/enum.html
Defining A simple Enum with underlying Integers values
Enum can be used to define sets of name constants
following code uses Enum to define the type GameStatus with """
from enum import Enum
GameStatus = Enum('GameStatus', ['PLAYING','WON','LOST', 'PAUSED'])
gamestatus1 = GameStatus.PLAYING
gamestatus2 = GameStatus.WON
gamestatus3 = GameStatus.LOST
gamestatus4 = GameStatus.PAUSED

print(gamestatus1)
Rolls = Enum('Rolls', [('EYES',2),( 'TREY',3) ,('SEVEN',7)])
print(Rolls.EYES.name)
print(Rolls.TREY.name)
print(Rolls.SEVEN.name)
print(Rolls.EYES.value)
print(Rolls.TREY.value)
print(Rolls.SEVEN.value)
#self documenting f-strings
if(Rolls.EYES.value == 2):
    print(gamestatus1)
if(Rolls.TREY.value == 3):
    print(gamestatus4)

number1 = 99
number2 = 100
number1, number2 = number2, number1
print(f'number1 = {number1}: number2 = {number2}')
#starred unpacking Expression in for statements
data = [(1,2,4,5),(6,7),
        (8,9,19)]
#loop the through the tuple at a time
#produces a list and
for first, *the_results in data:
    print(f"first: {first}, the_rest: {the_results}")