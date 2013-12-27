from space import Space
from tax_space import TaxSpace
from go_to_jail_space import GoToJailSpace


class GameBoard:

    def __init__(self):
        self.spaces = [
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
        self.size = len(self.spaces)

    def get_position(self, space_name):
        for space in self.spaces:
            if space.name == space_name:
                return self.spaces.index(space)
        

    def get_space(self, space_number):
        return self.spaces[space_number]
