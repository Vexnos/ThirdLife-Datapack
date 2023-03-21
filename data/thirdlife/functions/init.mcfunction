team add green "Green"
team modify green color green
team add yellow "Yellow"
team modify yellow color yellow
team add red "Red"
team modify red color red
team add grey "Grey"
team modify grey color gray
team join green @a
scoreboard objectives add Deaths deathCount
scoreboard players reset @a Deaths
scoreboard objectives add kills playerKillCount
scoreboard players reset @a kills
tag @a remove out