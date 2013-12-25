
from player import Player
from dice import Dice

class Game:

    def setup(self):
        self.number_of_players = int(raw_input("How many people are playing? "))
        self.players = [Player() for player in range(0,self.number_of_players)]
        self.current_player_index = 0
        self.board = [
            "Go",
            "Mediterranean Avenue",
            "Community Chest",
            "Baltic Avenut",
            "Income Tax",
            "Redding Railroad",
            "Oriental Avenue",
            "Chance",
            "Vermont Avenue",
            "Connecticut Avenue",
            "Jail",
            "St. Charles Place",
            "Electric Company",
            "States Avenue",
            "Virginia Avenue",
            "Pennsylvania Railroad",
            "St. James Place",
            "Community Chest",
            "Tennessee Avenue",
            "New York Avenue",
            "Free Parking",
            "Kentucky Avenue",
            "Chance",
            "Indiana Avenue",
            "Illinois Avenue",
            "B&O Railroad",
            "Atlantic Avenue",
            "Ventnor Avenue",
            "Waterworks",
            "Marvin Gardens",
            "Go To Jail",
            "Pacific Avenue",
            "Norh Carolina Avenue",
            "Community Chest",
            "Pennsylvania Avenue",
            "Short Line",
            "Chance",
            "Park Place",
            "Luxury Tax",
            "Boardwalk" ]

    def current_player_name(self):
        return self.players[self.current_player_index].name
        
    def start_turn(self):
        print "Start your turn, %s" % self.current_player_name()

    def end_turn(self):
        print "Your turn is over, %s" % self.current_player_name()
        self.current_player_index = self.current_player_index + 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0

    def roll_to_see_who_goes_first(self):
        dice = Dice()
        rollers = set(range(0, self.number_of_players))
        while len(rollers) != 1:
            print "Roll the dice to see who goes first!"
            highest_roll = 0
            highest_rollers = set()
            for roller in rollers:
                print ("It's %s's turn" % self.players[roller].name)
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

    def move_current_player(self, number_of_spaces):
        self.players[self.current_player_index].position_on_board += number_of_spaces
        print "%s is on %s" % (self.current_player_name(), self.board[self.players[self.current_player_index].position_on_board])
