
from space import Space

class CardSpace(Space):

    def __init__(self, name, deck):
        Space.__init__(self, name)
        self.deck = deck

    def handle_player_landing(self, player):
        Space.handle_player_landing(self, player)
        card = self.deck.next_card()
        card.handle_player(player)

