#!/usr/bin/env python3

try:
    from game_board import GameBoard
    from turn_maker import TurnMaker
    import os

    clear_screen = os.system('clear')

    print("\033[1;34m")
    print("_____        __    __                      _         ")
    print("| [] \      | |_  |  |                    | |        ")
    print("|  __/      |  _/ |  |_   ___   __   ___  | |        ")
    print("|  | __  __ | | _ | _  | |[] | |[]\ | []| | | __  __ ") 
    print("|__| \ \/ / |___/ |_||_| |___| | _/ |___| |_| \ \/ / ")
    print("     /  /                      |_|            /   /  ")
    print("     \_/                                      \_/    ")      
    print("\033[0;0m")
    print("Created by jwinnie and francispotter")
    print("Visit us on Github!")

    b = GameBoard()
    t = TurnMaker(b)

    clear_screen = os.system('clear')

    t.roll_to_see_who_goes_first()
    t.play()
    
except KeyboardInterrupt:
    os.system('clear')
    raise SystemExit
