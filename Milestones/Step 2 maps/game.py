import os
import msvcrt
import maps


x = 9
y = 4


os.system("mode con cols=135 lines=49")

#Displaying the map
def displayMap(maps,x,y):
    for x in range(len(maps)):
        map_row=str(maps[x]).replace(',', '').replace("'"," ").replace("."," ").replace("0","#")
        print(map_row)  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    displayMap(playerMapChoice,x,y) 

#selecting a map
mapChoice = maps.dungeonMap1
playerMapChoice= maps.playerMap1

#initialising the players position
position = mapChoice[0][0]


displayMap(playerMapChoice,x,y)

while position != "E":

    previousX = x
    previousY = y
    playerMapChoice[y][x] = "."
    print("Movement: W,S,D,A")
    movement = msvcrt.getch()

    if movement in {b'w', b'W'}:
        y = y-1
        position = mapChoice[y][x]
        playerMapChoice[y][x] = "@"
        

    if movement in {b's', b'S'}:
        y = y+1
        position = mapChoice[y][x]
        playerMapChoice[y][x] = "@"
        

    if movement in {b'd', b'D'}:
        x = x+1
        position = mapChoice[y][x]
        playerMapChoice[y][x] = "@"
        

    if movement in {b'a', b'A'}:
        x = x-1
        position = mapChoice[y][x]
        playerMapChoice[y][x] = "@"


    position = mapChoice[y][x]
    playerMapChoice[y][x] = "@"
    clear_screen()
    
    if position == "0" or position == "1":
        playerMapChoice[y][x] = "0"
        x = previousX
        y = previousY
        playerMapChoice[y][x] = "@"
        clear_screen()
        print("You hit a wall, you stumble in the darkness back to your previous position...")
        
    if position == ">":
        playerMapChoice[y][x] = ">"
        mapChoice=maps.dungeonMap2
        playerMapChoice=maps.playerMap2
        x=9
        y=4
        playerMapChoice[y][x] = "@"
        clear_screen()
        print("You walk down the stairs")


    if position == "<":
        playerMapChoice[y][x] = "<"
        mapChoice=maps.dungeonMap1
        playerMapChoice=maps.playerMap1
        x=9
        y=4
        playerMapChoice[y][x] = "@"
        clear_screen()
        print("You walk up the stairs")


