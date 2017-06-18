
class Card:

    def __init__(self, description):
        self.description = description

    def handle_player(self, player):
        print("You drew this card:")
        print("\033[3m\033[4m" + self.description + "\033[0m")
