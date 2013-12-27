from space import Space

class GoToJailSpace(Space):

    def handle_player_landing(self, player):
        Space.handle_player_landing(self, player)
        self.game.move_current_player_to_space("Jail")
        player.go_to_jail()
