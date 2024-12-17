#text based data interchange format
#Human -and- computer readable
#preferred for transmitting objects across platforms
#Similar format to python dictionaries
#Each json object contains a comma -separated list of propert names and values, in curly braces
#arrays
import json
accounts_dict = {'accounts': [
    {'accounts': 100, 'Name': 'Alan', 'balance': 1000},
    {'accounts': 310, "Name": "Emily", 'balance': 1500},
    {'accounts': 320, "Name": "Daniela", 'balance': 2000},
]} #python dictionary to write as javascript object notation

with open('accounts.json', 'w') as accounts_file:
    json.dump(accounts_dict, accounts_file) #dumb takes two argument, first argument is python object to turn into json
with open('accounts.json', 'r') as accounts_file:
    accounts_dict = json.load(accounts_file) #loads to file takes the arguments as
print(type(accounts_dict))
print(accounts_dict['accounts'])
print()
print(accounts_dict['accounts'][0])
with open('accounts.json', 'r') as accounts_file:
    print(json.dumps(json.load(accounts_file), indent=4))
grades_dict = {'gradebook':[{'student_id':23, 'name': 'Red', 'grade': 'A'},
                            {'student_id': 24, 'name': 'Wes', 'grade': 'B'},
                            {'student_id': 27, 'name': 'Sat', 'grade': 'A'},]}
with open('gradebook.json', 'w') as grades_file:
    json.dump(grades_dict, grades_file)
with open('gradebook.json', 'r') as grades_file:
    print(json.dumps(json.load(grades_file), indent=3))

#file oepn modes
"""r open file for reading
w open file for writing.Existing file is deleted
a open a text file for appending at the the end, create the file if it doesn't exist
r+ open a text file reading and writing
w+ open a text file writing and reading. existing files are delted
a+ open a text file for reading appending at the end, , new data is added at create the file if it doesn't exist
Read method returns a string containing the number of characters( or bytes for a binary file) specified by the method's integer argumen'
readline method Returns one line of text as string, including the newline character
returns an empty string on end of file
Writes methods writes a strings to a file
Classes for file objects are defines in the python standard Library's Io module 
https://docs.python.org/3/library/io.html"""
