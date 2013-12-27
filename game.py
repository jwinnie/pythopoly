
from player import Player
from dice import Dice
from space import Space
from tax_space import TaxSpace
from go_to_jail_space import GoToJailSpace

class Game:

    def setup(self):
        self.number_of_players = int(raw_input("How many people are playing? "))
        self.players = [Player() for player in range(0,self.number_of_players)]
        self.current_player_index = 0
        self.board = [
            Space("Go", self),
            Space("Mediterranean Avenue",self),
            Space("Community Chest",self),
            Space("Baltic Avenut",self),
            TaxSpace("Income Tax",self, 200),
            Space("Redding Railroad",self),
            Space("Oriental Avenue",self),
            Space("Chance",self),
            Space("Vermont Avenue",self),
            Space("Connecticut Avenue",self),
            Space("Jail",self),
            Space("St. Charles Place",self),
            Space("Electric Company",self),
            Space("States Avenue",self),
            Space("Virginia Avenue",self),
            Space("Pennsylvania Railroad",self),
            Space("St. James Place",self),
            Space("Community Chest",self),
            Space("Tennessee Avenue",self),
            Space("New York Avenue",self),
            Space("Free Parking",self),
            Space("Kentucky Avenue",self),
            Space("Chance",self),
            Space("Indiana Avenue",self),
            Space("Illinois Avenue",self),
            Space("B&O Railroad",self),
            Space("Atlantic Avenue",self),
            Space("Ventnor Avenue",self),
            Space("Waterworks",self),
            Space("Marvin Gardens",self),
            GoToJailSpace("Go To Jail",self),
            Space("Pacific Avenue",self),
            Space("Norh Carolina Avenue",self),
            Space("Community Chest",self),
            Space("Pennsylvania Avenue",self),
            Space("Short Line",self),
            Space("Chance",self),
            Space("Park Place",self),
            TaxSpace("Luxury Tax",self, 100),
            Space("Boardwalk",self )]

    def move_current_player_to_space(self, space_name):
        for space in self.board:
            if space.name == space_name:
                space_number = self.board.index(space)
                self.current_player().position_on_board = space_number


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

    def play(self):
        dice = Dice()
        while True:
            print
            self.start_turn()
            if self.current_player().in_jail:
                print "You are in jail."
                dice.roll()
                print dice.description_with_doubles()
                if dice.is_doubles():
                    print "You can move"
                    self.current_player().in_jail = False
                    self.move_current_player(dice.total())
                # They have to roll doubles
            else:
                roll_the_dice = True
                while roll_the_dice:
                    dice.roll()
                    print dice.description_with_doubles()
                    self.move_current_player(dice.total())
                    # Do things during the turn
                    roll_the_dice = dice.is_doubles()
            self.end_turn()


    def move_current_player(self, number_of_spaces):
        self.current_player().move(number_of_spaces, len(self.board))
        space = self.board[self.current_player().position_on_board]
        space.handle_player_landing(self.current_player())
        print "You have $%i" % self.current_player().cash
        if self.current_player().in_jail:
            print "You are in jail"
