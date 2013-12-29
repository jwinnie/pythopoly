# Represents a property that can be bought and owned

from space import Space

class PropertySpace(Space):

    def __init__(self, name, cost, rent):
        Space.__init__(self, name)
        self.cost = cost
        self.rent = rent
        self.status = 'AVAILABLE'

    def handle_player_landing(self, player):
        Space.handle_player_landing(self, player)
        if self.status == 'AVAILABLE':
            print "It costs $%i" % self.cost
            if player.cash >= self.cost:
                command = ""
                while not command:
                    command = raw_input("(B)uy (A)uction >").upper()
                if command == 'B':
                    player.pay_money(self.cost)
                    player.properties.append(self)
                    self.status = 'OWNED'
                    self.owner = player
                elif command == 'A':
                    pass
            else:
                print "You can't afford it."
        elif self.status == 'OWNED':
            print "It belongs to %s" % self.owner.name
            print "The rent is $%i" % self.rent
            amount_paid = player.pay_money(self.rent)
            self.owner.receive_money(amount_paid)


