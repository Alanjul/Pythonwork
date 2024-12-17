s1 = "Happy"
s2 = "birthday"
s1 += ' ' + s2
print(s1) #strings are immutable
#string repetition
symbol = '>'
symbol *= 5
print(symbol)
firstName = "Julius"
lastName = "Smith"
name = firstName + " " + lastName
number = len(name)
number *= "*"
print(number)
print(name)
print(number)
#stripping white spaces in strings

sentence = "      \t \nt This is a string. \t\t\n"
#sentence.strip() #leading and trailling white space is removed
print(sentence)
#strip left
sentence.rstrip()
print(sentence)
#strip right space
sentence.lstrip()
print(sentence)
name1 = "    Margo Magenta      "
print(name1.strip())
print(name1.lstrip())
print(name1.rstrip())

#string character case
string1 = "happy birthday"
print(string1.capitalize()) # first name name capitalize
print(string1.title())
text_string = "Happy new year"
print(text_string.capitalize())
print(text_string.title())
#comparizion withing


