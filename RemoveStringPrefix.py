import re
"""String method to remove string prefix and suffix
https:://peps.python.org/pep-0616
string removeprefix removes prefix from the start of string and
removes suffix from the end of string."""
string1 ="<<<string1<<<"
print(string1)
print(string1.removeprefix("<<<"))
print(string1.removesuffix("<<<"))

"""named unicode character in regular expression
re - regular expression operations
https:://docs.python.org/3/library/re.html
can use slash u or slash U to escape a sequence to insert a unicode
character into a string literals using a four digit or eight digit
hexidecimal code
such escape sequence may not be used in regular expression patterns
unicode character name at https://www.unicode.org/charts/charindex.html
Example below define simple_text with special unicode character  À"""
simple_text = "String with  À special unicode character"
print(simple_text)
#USE \N{name} to escape sequence and define character that matches  À
reg_pattern = r'\N{LATIN CAPITAL LETTER A WITH GRAVE}'
#print(reg_pattern)
match = re.search(reg_pattern, simple_text)
print(match.group())

