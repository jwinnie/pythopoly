from space import Space

class GoToJailSpace(Space):

    def handle_player_landing(self, player):
        Space.handle_player_landing(self, player)
        player.go_to_jail()
