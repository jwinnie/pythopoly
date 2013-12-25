
from dice import Dice

class Game:

    def setup(self):
        self.number_of_players = int(raw_input("How many people are playing? "))
        self.player_names = [raw_input("Player name: ") for i in range(0, self.number_of_players)]
        self.current_player_index = 0

    def current_player_name(self):
        return self.player_names[self.current_player_index]
        
    def start_turn(self):
        print "Start your turn, %s" % self.current_player_name()

    def end_turn(self):
        print "Your turn is over, %s" % self.current_player_name()
        self.current_player_index = self.current_player_index + 1
        if self.current_player_index >= len(self.player_names):
            self.current_player_index = 0

    def roll_to_see_who_goes_first(self):
        dice = Dice()
        rollers = set(range(0, self.number_of_players))
        while len(rollers) != 1:
            print "Roll the dice to see who goes first!"
            highest_roll = 0
            highest_rollers = set()
            for roller in rollers:
                print ("It's %s's turn" % self.player_names[roller])
                dice.roll()
                print dice.description()
                if dice.total() > highest_roll:
                    highest_roll = dice.total()
                    highest_rollers = set()
                if dice.total() == highest_roll:
                    highest_rollers.add(roller)
            rollers = highest_rollers
        self.current_player_index = highest_rollers.pop()
        print "%s goes first!" % self.current_player_name()
