from ast import Suite

from DataClasses import Card

c = Card(Card.FACE[0],Card.SUIT[1])
print(c)
print(c.faces)
print(c.suit)
print(c.image)
c2 = Card(Card.FACE[1],Card.SUIT[3])
c3 = Card(Card.FACE[2],Card.SUIT[1])
c.faces = 100
print(c.faces)
print(c)