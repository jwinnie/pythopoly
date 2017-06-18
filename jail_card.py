
from card import Card

class JailCard (Card):
    
    def __init__(self, description, go_to_jail):
        Card.__init__(self, description)
        self.go_to_jail = go_to_jail

    def handle_player(self, player):
        Card.handle_player(self, player)
        if self.go_to_jail:
            player.go_to_jail()
        if not self.go_to_jail:
            player.get_out_of_jail_cards += 1
        else:
            print("[pythopoly: jail_card.py] error: please specify type of jail card.")
