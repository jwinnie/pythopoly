
class Card:

    def __init__(self, description):
        self.description = description

    def handle_player(self, player):
        print "You drew this card:"
        print self.description
