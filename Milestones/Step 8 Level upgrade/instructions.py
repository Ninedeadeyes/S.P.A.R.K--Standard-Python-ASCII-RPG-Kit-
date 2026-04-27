
import msvcrt


def commands(Player):

    print("                  ")   
    print("                  ")
    print("Hero Stats ")
    print(f" Level:{Player.level} Health: {Player.health} Power: {Player.power} Gold: {Player.gold}")


    while True:        # ignores all non instruction keypress 
        
            movement = msvcrt.getch()

            if movement in {b'w', b'W'}:
                Player.y = Player.y-1
                break
                
            if movement in {b's', b'S'}:
                Player.y = Player.y+1
                break
        
            if movement in {b'd', b'D'}:
                Player.x = Player.x+1
                break
                
            if movement in {b'a', b'A'}:
                Player.x = Player.x-1
                break

