
from space import Space

class TaxSpace(Space):

    def __init__(self, name, game, tax_amount):
        Space.__init__(self, name, game)
        self.tax_amount = tax_amount

    def handle_player_landing(self, player):
        Space.handle_player_landing(self, player)
        player.cash -= self.tax_amount
