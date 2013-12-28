# Represents a property that can be bought and owned

from space import Space

class PropertySpace(Space):

    def __init__(self, name, cost):
        Space.__init__(self, name)
        self.cost = cost

    def handle_player_landing(self, player):
        Space.handle_player_landing(self, player)
        print "It costs $%i" % self.cost
        if player.cash >= self.cost:
            command = ""
            while not command:
                command = raw_input("(B)uy (A)uction >").upper()
            if command == 'B':
                player.cash -= self.cost
                player.properties.append(self)
            elif command == 'A':
                pass

