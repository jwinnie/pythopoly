
class Player:

    def __init__(self):
        self.name = raw_input("Player name: ")
        self.position_on_board = 0

    def move(self, spaces, board_size):
        self.position_on_board += spaces
        if self.position_on_board >= board_size:
            self.position_on_board = self.position_on_board % board_size
            self.passed_go = True
        else:
            self.passed_go = False
