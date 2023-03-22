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
def how_many_players():
    # Validates user input
    while True:
        try:
            amount_of_players = int(input("How many players do you have? "))
            return amount_of_players # Return the amount of players
        except ValueError:
            print("Invalid value entered! Please make sure your value is a number!")

def adding_players(amount_of_players):
    for i in range(amount_of_players): # Allows the user to add the amount of players to the game
        validating = True # Validates user input
        while validating:
            player_name = input("Add a player name here: ")
            if len(player_name) > 0: # Make sure the name is not just empty
                players.append(player_name)
                validating = False
            else:
                print("Invalid name entered, please try again")

    return players # Return the players

def roll():
    for player in players:
        life_roll = randint(2, 6)
        return life_roll

#-------Main-Routine-------
if __name__ == "__main__":
    # Defines the list of players
    players = []
    
    confirming = True
    while confirming:
        # Calls the function to get the amount of players in the game
        amount_of_players = how_many_players()
        # Calls the function for the user to add the players to the game
        players = adding_players(amount_of_players)

        # Confirm the roll, if not the user gets to start again
        confirm = input("Are you ready to roll your lives? (y/n): ")
        if confirm.lower().startswith("y"):
            confirming = False
        else:
            confirming = True
        
    # Roll the amount of lives for each player
    life_roll = roll()
    # Construct a dictionary out of the list of players and rolls
    players = {player : roll() for player in players}
    
    # Iterate through the dictionary, printing the key and value per iteration
    for key, value in players.items():
        print(key + " : " + str(value) + " Lives")