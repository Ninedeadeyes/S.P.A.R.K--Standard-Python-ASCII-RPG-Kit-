import subprocess
import msvcrt
import maps
import player

hero=player.Player(100,50,12,9,4)
gameloop=True

subprocess.run("mode con cols=135 lines=49", shell=True)

#Displaying the map
def displayMap(maps,x,y):
    for x in range(len(maps)):
        map_row=str(maps[x]).replace(',', '').replace("'"," ").replace("."," ").replace("0","#").replace("["," ").replace("]"," ")
        print(map_row)  

def clear_screen():
    print("\033[H\033[J", end="")
    displayMap(visualMapChoice,hero.x,hero.y) 

#selecting a map
dataMapChoice = maps.dataMap1       # Backend 
visualMapChoice= maps.visualMap1    # Frontend 

#initialising the players position in the backend 
position = dataMapChoice[hero.y][hero.x]

clear_screen()  # clears the screen and reprint map. 

while gameloop:
   
    previousX = hero.x                      # snapshot of current position just in case you hit into a wall 
    previousY = hero.y
    visualMapChoice[hero.y][hero.x] = "."   # it converts the previous position of the player back from @ to . 

    print("                  ")   
    print("                  ")
    print("Hero Stats ")
    print(f"Health: {hero.health} Power: {hero.power} Gold: {hero.gold}")
    movement = msvcrt.getch()

    if movement in {b'w', b'W'}:
        hero.y = hero.y-1
        position = dataMapChoice[hero.y][hero.x]
        visualMapChoice[hero.y][hero.x] = "@"
        

    if movement in {b's', b'S'}:
        hero.y = hero.y+1
        position = dataMapChoice[hero.y][hero.x]
        visualMapChoice[hero.y][hero.x] = "@"
        

    if movement in {b'd', b'D'}:
        hero.x = hero.x+1
        position = dataMapChoice[hero.y][hero.x]
        visualMapChoice[hero.y][hero.x] = "@"
        

    if movement in {b'a', b'A'}:
        hero.x = hero.x-1
        position = dataMapChoice[hero.y][hero.x]
        visualMapChoice[hero.y][hero.x] = "@"


    position = dataMapChoice[hero.y][hero.x]
    visualMapChoice[hero.y][hero.x] = "@"
    clear_screen()
    
    if position == "0" or position == "1":
        visualMapChoice[hero.y][hero.x] = "0"
        hero.x = previousX
        hero.y = previousY
        visualMapChoice[hero.y][hero.x] = "@"
        clear_screen()
        print("You hit a wall, you stumble in the darkness back to your previous position...")
        
    if position == ">":
        visualMapChoice[hero.y][hero.x] = ">"
        dataMapChoice=maps.dataMap2
        visualMapChoice=maps.visualMap2
        hero.x=9
        hero.y=4
        visualMapChoice[hero.y][hero.x] = "@"
        clear_screen()
        print("You walk down the stairs")


    if position == "<":
        visualMapChoice[hero.y][hero.x] = "<"
        dataMapChoice=maps.dataMap1
        visualMapChoice=maps.visualMap1
        hero.x=9
        hero.y=4
        visualMapChoice[hero.y][hero.x] = "@"
        clear_screen()
        print("You walk up the stairs")

    


