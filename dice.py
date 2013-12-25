
from random import randint

class Dice:

    def roll(self):
        raw_input("Press ENTER to roll the dice: ")
        self.values = (randint(1,6),randint(1,6))
    
    def total(self):
        return self.values[0] + self.values[1]

    def is_doubles(self):
        return self.values[0] == self.values[1]

    def description(self):
        return "A %i and a %i for a total of %i" % \
            (self.values[0], self.values[1], self.total())

    def description_with_doubles(self):
        return self.description() + (" -- Doubles!" if self.is_doubles() else  "")


