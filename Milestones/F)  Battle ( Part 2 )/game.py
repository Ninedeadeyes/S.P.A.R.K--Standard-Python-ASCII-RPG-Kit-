
import msvcrt
import subprocess
import events 
import maps
import player

hero=player.Player(100,50,12,9,4)  #(health,gold,power,x,y):
game_loop=True

subprocess.run("mode con cols=135 lines=49", shell=True)

#Displaying the map

def clear_screen():
    maps.visual_map_choice[hero.y][hero.x] = "@"   # prints player position in the frontend 
    print("\033[H\033[J", end="")
    maps.display_map(maps.visual_map_choice) 

def solid_interaction(object):      # Used for anything you can't go through eg : wall
    maps.visual_map_choice[hero.y][hero.x] = object 
    hero.x = previousX
    hero.y = previousY

def introduction ():
    print(" Adventure awaits !! ")

#initialising the players position in the backend 
position = maps.data_map_choice[hero.y][hero.x]

clear_screen()  # clears the screen and reprint map. 

introduction ()

while game_loop:

    if hero.alive==False:
        game_loop=False
   
    previousX = hero.x                      # snapshot of current position just in case you hit into a wall 
    previousY = hero.y
    
    maps.visual_map_choice[hero.y][hero.x] = "."   # it converts the previous position of the player back from @ to .  or it will leave a trail of @ @ @
    
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

    position = maps.data_map_choice[hero.y][hero.x]
    clear_screen()

    if position == ".":
        clear_screen()
        events.random_event(hero)

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
                maps.data_map_choice[hero.y][hero.x] = "."       # It removes the 'S' from the backend hence event won't be triggerd again. 
                                                            #  On the frontend it is a @ due to clear_screen() 
            else:
                solid_interaction("S")
                clear_screen()
            
        else:
            events.nothing_happened()  

        
    if position == ">":
        maps.visual_map_choice[hero.y][hero.x] = ">"
        maps.level+=1
        maps.data_map_choice=maps.data_maps_library[maps.level] 
        maps.visual_map_choice=maps.data_maps_library[maps.level] 

        if maps.level in maps.level_start_positions:                # generates hero starting position on the new map 
            coords = maps.level_start_positions[maps.level]
            hero.x = coords["x"]
            hero.y = coords["y"]

        clear_screen()
        print("You walk down the stairs")

    if position == "<":
        maps.visual_map_choice[hero.y][hero.x] = "<"
        maps.data_map_choice=maps.data_map_1
        maps.visual_map_choice=maps.visual_map_1
        maps.level=0
        hero.x=9
        hero.y=4
        clear_screen()
        print("You walk up the stairs")
