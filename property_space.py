# Represents a property that can be bought and owned

from space import Space

class PropertySpace(Space):

    def __init__(self, name, cost):
        Space.__init__(self, name)
        self.cost = cost

    def handle_player_landing(self, player):
        Space.handle_player_landing(self, player)
        print "It costs $%i" % self.cost

