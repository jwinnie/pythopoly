from space import Space
from tax_space import TaxSpace
from go_to_jail_space import GoToJailSpace
from property_space import PropertySpace
from card_space import CardSpace
from chance_card_deck import ChanceCardDeck

class GameBoard:

    def __init__(self):
        chance_deck = ChanceCardDeck()
        self.spaces = [
            Space("Go"),
            PropertySpace("Mediterranean Avenue",60,2),
            Space("Community Chest"),
            PropertySpace("Baltic Avenue",60,4),
            TaxSpace("Income Tax", 200),
            PropertySpace("Reading Railroad",200,25),
            PropertySpace("Oriental Avenue",100,6),
            CardSpace("Chance", chance_deck),
            PropertySpace("Vermont Avenue",100,6),
            PropertySpace("Connecticut Avenue",120,8),
            Space("Jail"),
            PropertySpace("St. Charles Place",140,10),
            PropertySpace("Electric Company",150,0),
            PropertySpace("States Avenue",140,10),
            PropertySpace("Virginia Avenue",160,12),
            PropertySpace("Pennsylvania Railroad",200,25),
            PropertySpace("St. James Place",180,14),
            Space("Community Chest"),
            PropertySpace("Tennessee Avenue",180,14),
            PropertySpace("New York Avenue",200,16),
            Space("Free Parking"),
            PropertySpace("Kentucky Avenue",220,18),
            CardSpace("Chance",chance_deck),
            PropertySpace("Indiana Avenue",220,18),
            PropertySpace("Illinois Avenue",240,20),
            PropertySpace("B&O Railroad",200,25),
            PropertySpace("Atlantic Avenue",260,22),
            PropertySpace("Ventnor Avenue",260,22),
            PropertySpace("Water Works",150,0),
            PropertySpace("Marvin Gardens",280,24),
            GoToJailSpace("Go To Jail"),
            PropertySpace("Pacific Avenue",300,26),
            PropertySpace("North Carolina Avenue",300,26),
            Space("Community Chest"),
            PropertySpace("Pennsylvania Avenue",320,28),
            PropertySpace("Short Line",200,25),
            CardSpace("Chance",chance_deck),
            PropertySpace("Park Place",350,35),
            TaxSpace("Luxury Tax", 100),
            PropertySpace("Boardwalk",400,50)]
        self.size = len(self.spaces)

    def get_position(self, space_name):
        for space in self.spaces:
            if space.name == space_name:
                return self.spaces.index(space)
        
    def get_space(self, space_number):
        return self.spaces[space_number]
