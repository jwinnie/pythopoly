from card import Card

class MoneyCard(Card):

    def __init__(self, description, amount):
        Card.__init__(self, description)
        self.amount = amount

    def handle_player(self, player):
        Card.handle_player(self, player)
        player.cash += self.amount
