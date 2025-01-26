import re
#ignore case sensitivity
results = re.search("Sam", "sam White", flags=re.IGNORECASE)
answer = results.group() if results  else "not defined"
print(answer)

#look for python at the begining with c
results1 = re.search("^Python", "sam White loves python", flags=re.IGNORECASE)
answer1 = results1.group() if results1 else "not defined"
print(answer1)
#using findall or find
contact = "Alan Julius 413-819-6214, home: 316-817-6214, work: 316-817-6217"
#using find all expressions
findcontact = re.findall(r"\d{3}-\d{3}-\d{4}", contact)
print(findcontact)
#using find iters
for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
    print(phone.group())
#capturing substrings within text message

text = 'Charlie Cyan, email: dem1@alan.com'
pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), email: (\w+@\w+\.\w{3})'
results3 =re.search(pattern, text) # searching for the entire regular expression
print(results3.groups())
print(results3.group())
#individual access
print(results3.group(1)) #first match
stringNumber = '10 + 5'
pattern_number =  r'(\d+) ([-+*/]) (\d+)'
results4 = re.search(pattern_number, stringNumber)
print(results4.group())
print(results4.group(1))
print(results4.group(2))
print(results4.group(3))