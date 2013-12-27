
from game_board import GameBoard
from turn_maker import TurnMaker

print "Welcome to Pythopoly!"
b = GameBoard()
t = TurnMaker()
t.setup(b)
t.roll_to_see_who_goes_first()
t.play()
