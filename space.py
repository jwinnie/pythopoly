
# Represents a space on the board

class Space:

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def handle_player_landing(self, player):
        print "You landed on %s" % self.name
