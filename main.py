
from dice import Dice
from game import Game

print "Welcome to Pythopoly!"
game = Game()
game.setup()
game.roll_to_see_who_goes_first()
game.play()
