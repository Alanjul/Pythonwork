"""Card class representing playing cards and its image file"""
class Card:
    #constants variables
    FACES = ['Ace','2','3','4','5','6','7','8','9','10',
             'Jack','Queen','King']
    SUITS = ['Club','Diamond','Heart','Spade']

    #initializing a card with a face and suit
    def __init__(self, face, suit):
        self._face = face
        self._suit = suit
    @property
    def face(self):
        #Return the cards's self face value
        return self._face
    @property
    def suit(self):
        #Returns the card suit
        return self._suit
    @property
    def name_image(self):
        """Returns the name of the card image"""
        base_name = str(self).replace(' ', '_').lower()

        # If the suit is "club", pluralize it manually.
        if "club" in base_name:
            base_name += 's'
        elif "diamond" in base_name:
            base_name += 's'
        elif "heart" in base_name:
            base_name += 's'
        elif "spade" in base_name:
            base_name += 's'

        # Return the file name with the .png extension
        return base_name + '.png'
        #return str(self).replace(' ','_').lower() + 's.png'
    @suit.setter
    def suit(self, suit):
        self._suit = suit
    def __repr__(self):
        """Returns a string representation of the card"""
        return f"Card(face={self.face}, suit={self.suit})"
    def __str__(self):
        """Returns a string representation of the card"""
        return f"{self.face} of {self.suit}"

    def __eq__(self, other):
        return self.face == other.face and self.suit == other.suit
    def __format__(self, format):
        """Returns a string representation of the card"""
        return f'{str(self)  : {format}}'