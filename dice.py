
from random import randint

class Dice:

    def roll(self):
        self.values = (randint(1,6),randint(1,6))
    
    def total(self):
        return self.values[0] + self.values[1]

    def is_doubles(self):
        return self.values[0] == self.values[1]

    def description(self):
        return "A %i and a %i for a total of %i%s" % \
            (self.values[0], self.values[1], self.total(),
              " -- Doubles!" if self.is_doubles() else  "")


