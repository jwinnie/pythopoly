from space import Space
from tax_space import TaxSpace
from go_to_jail_space import GoToJailSpace


class GameBoard:

    def __init__(self):
        self.spaces = [
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
            GoToJailSpace("Go To Jail"),
            Space("Pacific Avenue"),
            Space("Norh Carolina Avenue"),
            Space("Community Chest"),
            Space("Pennsylvania Avenue"),
            Space("Short Line"),
            Space("Chance"),
            Space("Park Place"),
            TaxSpace("Luxury Tax", 100),
            Space("Boardwalk" )]
        self.size = len(self.spaces)

    def get_position(self, space_name):
        for space in self.spaces:
            if space.name == space_name:
                return self.spaces.index(space)
        

    def get_space(self, space_number):
        return self.spaces[space_number]
