
class Game:

    def setup(self):
        number_of_players = raw_input("How many people are playing? ")
        self.player_names = [raw_input("Player name: ") for i in range(0, int(number_of_players))]
        self.current_player_index = 0

    def current_player_name(self):
        return self.player_names[self.current_player_index]
        
    def start_turn(self):
        print "Start your turn, %s" % self.current_player_name()

    def end_turn(self):
        print "Your turn is over, %s" % self.current_player_name()
        self.current_player_index = self.current_player_index + 1
        if self.current_player_index >= len(self.player_names):
            self.current_player_index = 0
    
        
    

    
