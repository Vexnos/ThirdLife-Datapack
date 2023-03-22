team add green "Green"
team modify green color green
team add yellow "Yellow"
team modify yellow color yellow
team add red "Red"
team modify red color red
team add grey "Grey"
team modify grey color gray
team add dark_green "Dark Green"
team modify dark_green color dark_green
scoreboard objectives add Deaths deathCount
scoreboard players reset @a Deaths
scoreboard objectives add kills playerKillCount
scoreboard players reset @a kills
scoreboard objectives add givelife trigger
scoreboard objectives add health health "❤"
scoreboard objectives modify health displayname {"text":"❤","color":"red"}
scoreboard objectives setdisplay belowName health
scoreboard players set @a Deaths 0
tag @a remove out