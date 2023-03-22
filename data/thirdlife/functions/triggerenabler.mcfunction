scoreboard players enable @a givelife
execute as @a[scores={givelife=1..},team=!red,team=!grey] run function thirdlife:givelife
execute as @a run scoreboard players set @a givelife 0