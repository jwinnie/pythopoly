import os
import time

class Player:

    def __init__(self, board):
        self.board = board
        self.name = input("Player name: ")
        self.cash = 2*500+4*100+50+20+2*10+5+5*1
        self.position = 0
        self.in_jail = False
        self.properties = []
        self.status = 'ACTIVE'
        self.get_out_of_jail_cards = 0

    def move_to_space(self, space_name):
        new_position = self.board.get_position(space_name)
        self.position = new_position

    def move(self, spaces):
        self.position += spaces
        if self.position >= self.board.size:
            self.position = self.position % self.board.size
            print("You passed Go! Collect \033[32m$200\033[0m")
            self.cash += 200
        space = self.board.get_space(self.position)
        space.handle_player_landing(self)
        if self.in_jail:
            print("You are in jail")

    def go_to_jail(self):
        if self.get_out_of_jail_cards > 0 and input("Use get out of jail card ({} left)? [y/n]") == 'y':
            self.get_out_of_jail_cards -= 1
        else:
            self.in_jail = True
            self.move_to_space("Jail")

    def do_turn(self, dice):
        print("\033[1m{}'s turn\033[0m".format(self.name))
        if self.in_jail:
            print("You are in jail.")
            dice.roll()
            dice.description_with_doubles()
            if dice.is_doubles():
                print("You can move")
                self.in_jail = False
                self.move(dice.total())
        else:
            roll_the_dice = True
            while roll_the_dice:
                space = self.board.get_space(self.position)
                print("You are on \033[93m{}\033[0m. You have \033[32m${}\033[0m".format(space.name, self.cash))
                dice.roll()
                dice.description_with_doubles()
                print()
                self.move(dice.total())
                # Do things during the turn
                roll_the_dice = dice.is_doubles()
                print()
        print("You own: " + ",".join([p.name for p in self.properties]))
        time.sleep(3)
 

    # Returns the amount actually paid

    def pay_money(self, amount_owed):
        if self.cash >= amount_owed:
            print("{} pays ${}".format(self.name, amount_owed))
            self.cash -= amount_owed
            amount_actually_paid = amount_owed
        else:
            print("{} owes \033[32m${}\033[0m but only has \033[32m${}\033[0m".format(self.name, amount, self.cash))
            amount_actually_paid = self.cash
            self.cash = 0
            self.status = 'BANKRUPT'
            print("{} is bankrupt".format(self.name))
        return amount_actually_paid

    def receive_money(self, amount):
        print("{} receives \033[32m${}\033[0m".format(self.name, amount))
        self.cash += amount
        return amount

    def receive_or_pay_money(self, amount):
        if amount > 0:
            return self.receive_money(amount)
        else:
            return 0-self.pay_money(0-amount)
