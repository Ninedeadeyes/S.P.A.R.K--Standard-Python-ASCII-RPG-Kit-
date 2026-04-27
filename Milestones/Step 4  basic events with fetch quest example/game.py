
import msvcrt
import random
import subprocess

import events 
import maps
import player
import random

hero=player.Player(100,50,12,9,4)
game_loop=True
level=0   # because 1st position/index in a list is a 0  hence 1st map is 0 and the 2nd map is 1 etc etc 

subprocess.run("mode con cols=135 lines=49", shell=True)

#Displaying the map
def display_map(maps):
    for x in range(len(maps)):
        map_row=str(maps[x]).replace(',', '').replace("'"," ").replace("."," ").replace("["," ").replace("]"," ")
        print(map_row)  

def clear_screen():
    visual_map_choice[hero.y][hero.x] = "@"   # prints player position in the frontend 
    print("\033[H\033[J", end="")
    display_map(visual_map_choice) 

def solid_interaction(object):      # Used for anything you can't go through eg : wall
    visual_map_choice[hero.y][hero.x] = object 
    hero.x = previousX
    hero.y = previousY

def introduction ():
    print(" Adventure awaits !! ")

#selecting a map
data_map_choice = maps.data_maps_library[level]     # Backend 
visual_map_choice= maps.visual_maps_library[level]  # Frontend 

#initialising the players position in the backend 
position = data_map_choice[hero.y][hero.x]

clear_screen()  # clears the screen and reprint map. 

introduction ()


while game_loop:
   
    previousX = hero.x                      # snapshot of current position just in case you hit into a wall 
    previousY = hero.y
    
    visual_map_choice[hero.y][hero.x] = "."   # it converts the previous position of the player back from @ to .  or it will leave a trail of @ @ @

    print("                  ")   
    print("                  ")
    print("Hero Stats ")
    print(f"Health: {hero.health} Power: {hero.power} Gold: {hero.gold}")

    while True:        # ignores all non instruction keypress 
    
        movement = msvcrt.getch()

        if movement in {b'w', b'W'}:
            hero.y = hero.y-1
            break
            
        if movement in {b's', b'S'}:
            hero.y = hero.y+1
            break
       
        if movement in {b'd', b'D'}:
            hero.x = hero.x+1
            break
            
        if movement in {b'a', b'A'}:
            hero.x = hero.x-1
            break

    position = data_map_choice[hero.y][hero.x]
    clear_screen()

    if position == ".":
        clear_screen()

        r=random.random()                    
        if r < 0.91 :                        
            events.nothing_happened()                         
                  
        else:
            events.loot(hero)

    if position == "#":
        solid_interaction("#")
        clear_screen()
        print("You hit a wall..")

    if position == "G":
        solid_interaction("G")
        clear_screen()
        events.goblin_spoon_quest(hero)

    if position=="S":

        if hero.got_spoon_for_quest==False:
            taken=events.spoon_found(hero)
            if taken:
                data_map_choice[hero.y][hero.x] = "."       # It removes the 'S' from the backend hence event won't be triggerd again. 
                                                            #  On the frontend it is a @ due to clear_screen() 
            else:
                solid_interaction("S")
                clear_screen()
            
        else:
            events.nothing_happened()  

        
    if position == ">":
        visual_map_choice[hero.y][hero.x] = ">"
        level+=1
        data_map_choice=maps.data_maps_library[level] 
        visual_map_choice=maps.data_maps_library[level] 

        if level in maps.level_start_positions:                # generates hero starting position on the new map 
            coords = maps.level_start_positions[level]
            hero.x = coords["x"]
            hero.y = coords["y"]

        clear_screen()
        print("You walk down the stairs")

    if position == "<":
        visual_map_choice[hero.y][hero.x] = "<"
        data_map_choice=maps.data_map_1
        visual_map_choice=maps.visual_map_1
        level=0
        hero.x=9
        hero.y=4
        clear_screen()
        print("You walk up the stairs")