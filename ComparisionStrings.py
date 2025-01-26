print(f"A: {ord('A')}; a: {ord('a')}" )# gives the numerical of each character
#comparison
string1 = "Orange"
string2 ="orange"
print(string1 == string2)
print(string1 != string2)
print(string1 > string2)
print(string1 < string2)
#searching for substrings
sentence = "to be or not to be that is the question"
print(sentence.count("to"))
#start from index 12 search for to
print(sentence.count("to",12, 25))
#physical location look of a substring
print(sentence.index("be") )# first occurence
#search backwards
print(sentence.rindex("be")) # causes value errror not founde
#use find to avoid erros
print(sentence.find("I"))
print ("that" in sentence) # will return true case sentence
print("that"  not in sentence)
#search at the begin
#print(sentence.startswith("to"))
print(sentence.startswith("be"))
sentence2 = "to be or not to be that is the question"
for  word in sentence2.split():
    if word.startswith("t"):
        print(word, end=" ")
print()
values = "1\t2\t3\t4\t5"
print(values.replace("\t",", "))
substring1 = '1 2 3 4 5'
print(substring1.replace(" "," --->"))
#split and Join Strings
letters = "A, B, C, D" # split with a comma
letters2 = letters.split(",")
letters3 = letters.split(",", 2) # spliting the maximum of 2
print(letters3)
print(letters2)
letters_lists = ["B", "D", "E", "F"]
#joining the strings as a comma delimited list

print(", ".join(letters_lists))
#join values from 0 to 9 as strings
values1 = ",".join([str(i) for i in range(1, 11)])
print(values1)
#partitioning a string
string4 = "Amanda: 89, 97, 92".partition(": ")
print(string4)
#rpartition
url="http://python.org/books/html"
rest_of_line, separator, document = url.rpartition("/") #partitioning backwords
print(rest_of_line)
print(separator)
print(document)
#splitting lines
lines = """
This is the line 
the line starts
the line ends with 3"""
print(lines)
print(lines.splitlines(True))
print(lines.splitlines(False))
formatName = "Pamela White"

joinName = ', '.join(reversed(formatName.split( )))
print(joinName)

"""urlString = "http://www.deitel.com/books/pycds/table_of_contents.html"
first_url, second_url, third_ul = urlString.partition( "://")
host, port, document = third_ul.partition("/")
print(host)
path, separate, name = document.rpartition("/")
print(path)"""

ustring2 = "https:://www.deitel.com/books/pycds/table_of_contents.html"
firsts_url, seconds, thirds = ustring2.partition("//")
print(firsts_url)
print(seconds) #prints//
ports, hosts, documents = thirds.partition("/")
print(ports)
print(hosts)
topic, subtopic, content = documents.rpartition("/")
print(content) #prints table of content
print("-27".isdigit()) # prints False because of a negative
print("27".isdigit())  #prints true

#is it a number or a letter
print("A1876B".isalnum())  #prints true
print("4122 Thomposon street".isalnum())  #prints false
pathfile = r"c::\\juliu\\document\\pycharm\\stringDeep"
filepath = r'c::\juliu\downloads\textbook' #raw string
print(filepath)
print(pathfile)