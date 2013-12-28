
from card import Card

class GoToSpaceCard(Card):

    def __init__(self, description, space_name):
        Card.__init__(self, description)
        self.space_name = space_name

    def handle_player(self, player):
        Card.handle_player(self, player)
        player.move_to_space(self.space_name)
