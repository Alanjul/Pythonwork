from CardShuffling import Card
import random
class DeckOfCard:
    NUMBER_OF_CARDS = 52 #constant number of cards
    def __init__(self):
        """Initialize a Deck of Cards"""
        self._cards = []
        self._current_card = 0
        for count in range(DeckOfCard.NUMBER_OF_CARDS):
            self._cards.append(Card(Card.FACES[count%13],
                                   Card.SUITS[count//13]))
    def shuffle(self):
        """Shuffle the cards"""
        random.shuffle(self._cards)
    def deal_card(self):
        "Return one card from the deck"
        try:
            #get the card at the current position for the decks list
            card = self._cards[self._current_card]
            # increment index and make sure it doesn't go out of bounds
            self._current_card = (self._current_card + 1) % len(self._cards)
            return card #return the card
        except IndexError:
            raise IndexError("Deck of cards out of range")
    def __str__(self):
        """Return a string representation of the current card"""
        s= ''
        for index, card in enumerate(self._cards):
            s += f'{self._cards[index]:<19} ' #left aligned 19 strings
            if (index +1) % 4 ==0:
                s += '\n' #insert new line character after 4 cards
        return s




