

import os
import msvcrt


# map  dungeonMap=Backend Data ( the logic in the back ground )  playerMap=Visual Data (What the player sees) 


dungeonMap = [["0","0","0","0","0","0","0","0","0"],
              ["0",".",".","0",".",".",".",".","0"],
              ["0",".",".",".",".",".",".","0","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".","0",".",".",".","0"],
              ["0",".","0","0",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0","0","0","0","0","0","0","0","0"]]

playerMap  = [["0","0","0","0","0","0","0","0","0"],
              ["0",".",".","0",".",".",".",".","0"],
              ["0",".",".",".",".",".",".","0","0"],
              ["0","@",".",".",".",".",".",".","0"],
              ["0",".",".",".","0",".",".",".","0"],
              ["0",".","0","0",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0","0","0","0","0","0","0","0","0"]]


x = 1
y = 3

os.system("mode con cols=135 lines=49")

#Displaying the map
def displayMap(maps):    #Displaying the map
    for x in range(len(maps)):
        map_row=str(maps[x]).replace(',', '').replace("'"," ").replace("."," ").replace("0","#")
        print(map_row)  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    displayMap(playerMap)

#selecting a map
mapChoice = dungeonMap

#initialising the players position  (backend)
position = mapChoice[0][0]


displayMap(playerMap)

while position != "E":

    previousX = x
    previousY = y
    playerMap[y][x] = "."
    print("Movement: W,S,D,A")
    movement = msvcrt.getch()

    if movement in {b'w', b'W'}:
        y = y-1
        position = mapChoice[y][x]
        playerMap[y][x] = "@"
        

    if movement in {b's', b'S'}:
        y = y+1
        position = mapChoice[y][x]
        playerMap[y][x] = "@"
        

    if movement in {b'd', b'D'}:
        x = x+1
        position = mapChoice[y][x]
        playerMap[y][x] = "@"
        

    if movement in {b'a', b'A'}:
        x = x-1
        position = mapChoice[y][x]
        playerMap[y][x] = "@"


    position = mapChoice[y][x]
    playerMap[y][x] = "@"
    clear_screen()
    
    if position == "0" or position == "1":
        playerMap[y][x] = "0"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen()
        print("You hit a wall, you stumble in the darkness back to your previous position...")
        



