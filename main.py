
from dice import Dice
from game import Game

print "Welcome to Pythopoly!"
game = Game()
game.setup()



dice = Dice()

print "Roll the dice to see who goes first!"
for player in game.player_names:
    raw_input (player)
    dice.roll()
    print dice.description()
    

while True:
    print
    game.start_turn()
    raw_input("Press ENTER to roll:")
    dice.roll()
    print dice.description()
    game.end_turn()
