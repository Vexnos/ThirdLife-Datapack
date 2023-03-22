execute as @s at @s run tellraw @s ["",{"text":"You gave a life to ","color":"white"},{"selector":"@p[distance=0.01..,team=!grey]"}]
execute as @s at @s run tellraw @p[distance=0.01..,team=!grey] ["",{"text":"You received a life from ","color":"white"},{"selector":"@s"}]
execute as @s at @s run particle totem_of_undying ~ ~1 ~ 1 1 1 0 50 normal @a
execute as @s at @s run playsound item.totem.use master @a ~ ~ ~ .75 1
execute as @s at @s at @p[distance=0.01..,team=!grey] run particle happy_villager ~ ~1 ~ 1 1 1 0 50 normal @a
execute as @s at @s run title @p[distance=0.01..,team=!grey] title {"text":"You recieved a life","color":"green"}
execute as @s at @s run scoreboard players remove @p[distance=0.01..,team=!grey] Deaths 1
execute as @s at @s run scoreboard players add @s[team=!red,team=!grey] Deaths 1
execute as @a run scoreboard players set @a givelife 0