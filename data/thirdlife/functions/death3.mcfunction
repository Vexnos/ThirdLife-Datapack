execute as @a run execute if score @s Deaths matches 3.. run gamemode spectator @s
execute as @a run execute if score @s Deaths matches 3.. run team join grey @s
execute as @a[tag=!out] if score @s Deaths matches 3.. run title @s title {"text":"You are out of lives!","italic":"false","color":"red"}
execute as @a[tag=!out] at @s if score @s Deaths matches 3.. run playsound entity.ender_dragon.growl master @s ~ ~ ~ 100 1
execute as @a[tag=!out] if score @s Deaths matches 3.. run tag @s add out
