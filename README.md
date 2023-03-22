# Third Life
This is a Third Life datapack created my me, inspired by Grian's Third Life series. 
Go check it out if you haven't: https://www.youtube.com/watch?v=nszciRXXJZk&list=PLU2851hDb3SHLdAlj8dxqHPeT_qIBbRBv

For a player size of 4 or above, I recommend a worldborder cap of 1000 for the best experience.

To start the game, have everyone on the server and run `/function thirdlife:init`.

This current version of Third Life has the Boogeyman partially implemented. The Boogeyman was introduced in Season 2 of Third Life known as Last Life.
To start the Boogeyman, run `/function thirdlife:boogeyinit`.

This current version of Third Life has Life Transferring implemented, run `/trigger givelife` and make sure the person you want to give the life to is the closest player to you and the life should transfer. You cannot give lives to people who are out, red names can't give lives to people as they would be out.


There is a random life generator made in Python if you wish to use it. To use it, create a text file called `players.txt` in the same folder as the Python script. How to format:
```
player_1
player_2
player_3
etc...
```
Then run the Python script and it will roll the amount of lives for each player, enjoy!