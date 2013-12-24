
from dice import Dice
from game import Game

print "Welcome to Pythopoly!"
game = Game()
game.setup()



dice = Dice()

rollers = set(range(0, game.number_of_players))
while len(rollers) != 1:
    print "Roll the dice to see who goes first!"
    highest_roll = 0
    highest_rollers = set()
    for index in range(0, len(rollers)):
        raw_input("%s, press ENTER to roll:" % game.player_names[index])
        dice.roll()
        print dice.description()
        if dice.total() > highest_roll:
            highest_roll = dice.total()
            highest_rollers = set()
        if dice.total() == highest_roll:
            highest_rollers.add(index)
    rollers = highest_rollers

game.current_player_index = highest_rollers.pop()

while True:
    print
    game.start_turn()
    raw_input("Press ENTER to roll:")
    dice.roll()
    print dice.description()
    game.end_turn()
