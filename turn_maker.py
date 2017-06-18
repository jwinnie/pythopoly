
from game_board import GameBoard
from player import Player
from dice import Dice
import time
import os

class TurnMaker:

    def __init__(self, board):
        print("\033[0m")
        self.number_of_players = int(input("How many people are playing? "))
        self.players = []
        for player in range(0,self.number_of_players):
            new_player = Player(board)
            self.players.append(new_player)
        self.current_player = self.players[0]

    def play(self):
        dice = Dice()
        while True:
            self.current_player.do_turn(dice)
            os.system('clear')
            current_player_index = self.players.index(self.current_player)
            next_player_index = (current_player_index + 1) % len(self.players)
            self.current_player = self.players[next_player_index]

    def roll_to_see_who_goes_first(self):
        dice = Dice()
        rollers = set(range(0, self.number_of_players))
        while len(rollers) != 1:
            highest_roll = 0
            highest_rollers = set()
            for roller in rollers:
                print("\033[1m{}, roll to see who goes first...\033[0m".format(self.players[roller].name))
                dice.roll()
                dice.description()
                if dice.total() > highest_roll:
                    highest_roll = dice.total()
                    highest_rollers = set()
                if dice.total() == highest_roll:
                    highest_rollers.add(roller)
                time.sleep(2)
                os.system('clear')
            rollers = highest_rollers
        self.current_player = self.players[highest_rollers.pop()]
        print("\033[1m{} goes first!\033[0m".format(self.current_player.name))
        print()








