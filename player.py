
class Player:

    def __init__(self, board):
        self.board = board
        self.name = raw_input("Player name: ")
        self.cash = 2*500+4*100+50+20+2*10+5+5*1
        self.position = 0
        self.in_jail = False

    def move_to_space(self, space_name):
        new_position = self.board.get_position(space_name)
        self.position = new_position

    def move(self, spaces):
        self.position += spaces
        if self.position >= self.board.size:
            self.position = self.position % self.board.size
            print "You passed Go! Collect $200"
            self.cash += 200
        space = self.board.get_space(self.position)
        space.handle_player_landing(self)
        print "You have $%i" % self.cash
        if self.in_jail:
            print "You are in jail"

    def go_to_jail(self):
        self.in_jail = True
        self.move_to_space("Jail")

    def do_turn(self, dice):
        print
        print
        print "Start your turn, %s" % self.name
        print
        if self.in_jail:
            print "You are in jail."
            dice.roll()
            print dice.description_with_doubles()
            if dice.is_doubles():
                print "You can move"
                self.in_jail = False
                self.move(dice.total())
        else:
            roll_the_dice = True
            while roll_the_dice:
                dice.roll()
                print dice.description_with_doubles()
                self.move(dice.total())
                # Do things during the turn
                roll_the_dice = dice.is_doubles()
        print "Your turn is over, %s" % self.name

            
