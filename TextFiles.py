"""sys.stdin standard input streams reads input from command line
sys.stdout standard output stream
sys.stderr standard error stream"""
import sys

#writing text into files using a with statement
# to acquire the resource and used then give it back
#open function will take two arguments name file and mode of how the file will open

with open('accounts.txt', mode='w') as accounts:

    accounts.write('100 jones 24.97\n')
    accounts.write('200  Doe  345.67\n')
    accounts.write('300  white  045.67\n')
    accounts.write('500  black  224.67\n')

with open('grades.txt', mode='w') as grades:

    grades.write('   1    Green    B\n')
    grades.write('   2    Yellow   A\n')
    grades.write('   3    White    B\n')
with open('accounts.txt', mode='r') as accounts:
    print(f"{'Accounts': <10} {"Name": <10} {"Balance":<10}")
    for record in accounts:
        accounts, name, balance = record.split()
        print(f"{accounts:<10} {name:<10} {balance:<10}")

