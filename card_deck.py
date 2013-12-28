
from random import shuffle

class CardDeck:

    def __init__(self):
        self.shuffle_deck()

    def shuffle_deck(self):
        self.deck = [card for card in self.cards]
        shuffle(self.deck)

    def next_card(self):
        if len(self.deck) == 0:
            self.shuffle_deck()
        return self.deck.pop()

