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

#-------Functions-------
def roll():
    for player in players:
        life_roll = randint(2, 6)
        return life_roll

#-------Main-Routine-------
if __name__ == "__main__":
    # Defines the list of players
    players = []
    # Opens the players text file
    players_list = open('players.txt', 'r')
    # Reads the lines of the text file
    lines = players_list.readlines()

    # Iterates over lines to retrieve player names
    for line in lines:
        players.append(line.strip()) # Strips the players of the new line character
        
    # Roll the amount of lives for each player
    life_roll = roll()
    # Construct a dictionary out of the list of players and rolls
    players = {player : roll() for player in players}
    
    # Iterate through the dictionary, printing the key and value per iteration
    for key, value in players.items():
        print(key + " : " + str(value) + " Lives")