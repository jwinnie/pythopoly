
from random import randint
import time

class Dice:

    def roll(self):
        input("Press ENTER to roll the dice: ")
        self.values = (randint(1,6),randint(1,6))
    
    def total(self):
        return self.values[0] + self.values[1]

    def is_doubles(self):
        return self.values[0] == self.values[1]

    def description(self):
        print("[ \033[1mDICE: \033[0mA \033[1m{}\033[0m and a \033[1m{}\033[0m for a total of \033[1m{}\033[0m ]".format(self.values[0], self.values[1], self.total()))
        time.sleep(1)

    def description_with_doubles(self):
        self.description()
        if self.is_doubles():
            print("\033[35mDoubles!\033[0m")

