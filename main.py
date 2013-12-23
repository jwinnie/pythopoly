
from dice import Dice
from game import Game

print "Welcome to Pythopoly!"
game = Game()
game.start()



dice = Dice()




while True:
    print
    game.start_turn()
    raw_input("Press ENTER to roll:")
    dice.roll()
    print dice.description()
    game.end_turn()
