
from dice import Dice
from game import Game

print "Welcome to Pythopoly!"
game = Game()
game.setup()
game.roll_to_see_who_goes_first()
dice = Dice()
while True:
    print
    game.start_turn()
    roll_the_dice = True
    while roll_the_dice:
        dice.roll()
        print dice.description_with_doubles()
        game.move_current_player(dice.total())
        # Do things during the turn
        roll_the_dice = dice.is_doubles()
    game.end_turn()
