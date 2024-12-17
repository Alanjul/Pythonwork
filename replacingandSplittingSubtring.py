import re
replaceTabs= re.sub(r'\t', ', ', '1\t2\t3\t4')
print(replaceTabs)
#replacing the first two tabs
replaceFirst2Tabs = re.sub(r'\t', ', ', '1\t2\t3\\t4', count=2)
print(replaceFirst2Tabs)
#spliting the subtrings
splitStrings = re.split(r',\s*', '1,2,3,4,    5,6,7,8') # creates a list of substrings
print(splitStrings)
#maxsplit to specifiy the number of splits necessary
maxSplit = re.split(r',\s*', '1,2,3,4,    5,6,7,8', maxsplit=3)
print(maxSplit)

#replace the tables adjacents ONE OR MOERE
adjacent_tabs_replaced = re.sub(r'\t+', ',  ', 'A\tB\tC\t\t\tD')
print(adjacent_tabs_replaced)

split_function = re.split(r'\$+', '123$Main$$Street')
print(split_function)
#using search function to find the first match in the string and returns none if the match is not found
#returns the data object SRE_MATCH
result = re.search("Python", "Python is good for Artificial Intelligence")
print(result)
results = re.search("Hello", "Python is fun")
answer = result.group() if results else " not found"
print(answer)

