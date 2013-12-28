
# Represents a space on the board

class Space:

    def __init__(self, name):
        self.name = name

    def handle_player_landing(self, player):
        print "You landed on %s" % self.name
