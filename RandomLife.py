'''
-------------------------------
   File: RandomLife.py
Project: Random Life generation
 Author: Vexnos
   Date: 2023-03-22
-------------------------------
'''
#-------Libraries-------
from random import randint

#-------Main-Routine-------
if __name__ == "__main__":
    # Opens the players text file
    with open('players.txt', 'r') as players_list:
        # Reads the lines of the text file
        lines = players_list.readlines()

    # Iterates over lines to retrieve player names
    players = [line.strip() for line in lines]

    # Loops the program until the user quits
    rolling = True
    while rolling:
        bar = "-" * 30
        print(f"{bar}\nRolls\n{bar}")

        # Iterates over each player in the list and rolls for them
        for player in players:
            print(f"{player} : {randint(2, 6)}")

        # Allows the user to roll again
        roll_again = input(f"{bar}\nWant to roll again? (y/n): ")
        rolling = roll_again.lower().startswith("y")