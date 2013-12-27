
from player import Player
from dice import Dice
from space import Space
from tax_space import TaxSpace

class Game:

    def setup(self):
        self.number_of_players = int(raw_input("How many people are playing? "))
        self.players = [Player() for player in range(0,self.number_of_players)]
        self.current_player_index = 0
        self.board = [
            Space("Go"),
            Space("Mediterranean Avenue"),
            Space("Community Chest"),
            Space("Baltic Avenut"),
            TaxSpace("Income Tax", 200),
            Space("Redding Railroad"),
            Space("Oriental Avenue"),
            Space("Chance"),
            Space("Vermont Avenue"),
            Space("Connecticut Avenue"),
            Space("Jail"),
            Space("St. Charles Place"),
            Space("Electric Company"),
            Space("States Avenue"),
            Space("Virginia Avenue"),
            Space("Pennsylvania Railroad"),
            Space("St. James Place"),
            Space("Community Chest"),
            Space("Tennessee Avenue"),
            Space("New York Avenue"),
            Space("Free Parking"),
            Space("Kentucky Avenue"),
            Space("Chance"),
            Space("Indiana Avenue"),
            Space("Illinois Avenue"),
            Space("B&O Railroad"),
            Space("Atlantic Avenue"),
            Space("Ventnor Avenue"),
            Space("Waterworks"),
            Space("Marvin Gardens"),
            Space("Go To Jail"),
            Space("Pacific Avenue"),
            Space("Norh Carolina Avenue"),
            Space("Community Chest"),
            Space("Pennsylvania Avenue"),
            Space("Short Line"),
            Space("Chance"),
            Space("Park Place"),
            TaxSpace("Luxury Tax", 100),
            Space("Boardwalk" )]

    def current_player(self):
        return self.players[self.current_player_index]
        
    def current_player_name(self):
        return self.current_player().name
        
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
        self.current_player().move(number_of_spaces, len(self.board))
        if self.current_player().passed_go:
            print "You passed Go!"
        space = self.board[self.current_player().position_on_board]
        space.handle_player_landing(self.current_player())
        print "You have $%i" % self.current_player().cash

