from collections import namedtuple
#creating class of a namedtuple with two attributes face and suit
Card = namedtuple('Card', ['face', 'suit'])
#instances of Card object being created
card = Card(face="Ace", suit="Spades")
print(card.face) #access the card face field instance attribute
print(card.suit) #access the card suit of the card instance which holds Spade values
print(card) #print string representation of named tuple
values = ['Queen', 'Diamond'] #list of values
#_make method from nametuple to create an instance of Card object to create a list tuple
valuesmake =  card._make(values)
print(valuesmake)
print("The ordered dictionary")
print(valuesmake._asdict()) #return ordered dictionary of list tuple
