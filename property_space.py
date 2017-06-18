# Represents a property that can be bought and owned

from space import Space
import time

class PropertySpace(Space):

    def __init__(self, name, cost, rent):
        Space.__init__(self, name)
        self.cost = cost
        self.rent = rent
        self.status = 'AVAILABLE'

    def handle_player_landing(self, player):
        Space.handle_player_landing(self, player)
        if self.status == 'AVAILABLE':
            print("It's available and costs \033[32m${}\033[0m.".format(self.cost))
            if player.cash >= self.cost:
                print("Do you want to buy it? If not, it will be auctioned.")
                while True:
                    command = input("[y/n]> ").upper()
                    if command == 'Y':
                        player.pay_money(self.cost)
                        player.properties.append(self)
                        self.status = 'OWNED'
                        self.owner = player
                        time.sleep(1)
                        break

                    elif command == 'N':
                        break
                    else:
                        print("Please enter 'y' or 'n'")
                        pass
                    
            else:
                print("You can't afford it.")
        elif self.status == 'OWNED':
            if player == self.owner:
                print("You own it!")
            else:
                print("It belongs to {}".format(self.owner.name))
                print("The rent is \033[32m${}\033[0m".format(self.rent))
                amount_paid = player.pay_money(self.rent)
                self.owner.receive_money(amount_paid)


