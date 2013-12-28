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
            PropertySpace("Mediterranean Avenue",60),
            Space("Community Chest"),
            PropertySpace("Baltic Avenue",60),
            TaxSpace("Income Tax", 200),
            PropertySpace("Reading Railroad",200),
            PropertySpace("Oriental Avenue",100),
            CardSpace("Chance", chance_deck),
            PropertySpace("Vermont Avenue",100),
            PropertySpace("Connecticut Avenue",120),
            Space("Jail"),
            PropertySpace("St. Charles Place",140),
            PropertySpace("Electric Company",150),
            PropertySpace("States Avenue",140),
            PropertySpace("Virginia Avenue",160),
            PropertySpace("Pennsylvania Railroad",200),
            PropertySpace("St. James Place",180),
            Space("Community Chest"),
            PropertySpace("Tennessee Avenue",180),
            PropertySpace("New York Avenue",200),
            Space("Free Parking"),
            PropertySpace("Kentucky Avenue",220),
            CardSpace("Chance",chance_deck),
            PropertySpace("Indiana Avenue",220),
            PropertySpace("Illinois Avenue",240),
            PropertySpace("B&O Railroad",200),
            PropertySpace("Atlantic Avenue",260),
            PropertySpace("Ventnor Avenue",260),
            PropertySpace("Water Works",150),
            PropertySpace("Marvin Gardens",280),
            GoToJailSpace("Go To Jail"),
            PropertySpace("Pacific Avenue",300),
            PropertySpace("North Carolina Avenue",300),
            Space("Community Chest"),
            PropertySpace("Pennsylvania Avenue",320),
            PropertySpace("Short Line",200),
            CardSpace("Chance",chance_deck),
            PropertySpace("Park Place",350),
            TaxSpace("Luxury Tax", 100),
            PropertySpace("Boardwalk",400)]
        self.size = len(self.spaces)

    def get_position(self, space_name):
        for space in self.spaces:
            if space.name == space_name:
                return self.spaces.index(space)
        
    def get_space(self, space_number):
        return self.spaces[space_number]
