import msvcrt   
import random
import maps
import events


def fight (Player,Enemy):
        
        print("\033c", end="")
        battle=True 
        print("An enemy appears, ready to fight")
    
        while battle==True:

            print(f"{Enemy.name} hp:{Enemy.health} Power:{Enemy.power}")
            print("                                                                                                                                                   ")
            print(f"Player hp:{Player.health} Power:{Player.power}")
            print("What is your next action: Attack (A), Escape(E)")

            while True:
                 
                 choice = msvcrt.getch()

                 if choice in {b'a', b'A'}:
                
                    enemy_dice_roll=random.randint(1,6)
                    player_dice_roll=random.randint(1,6)
                    enemy_damage_total=max(0,Enemy.power+enemy_dice_roll)
                    Player.health-=enemy_damage_total
                    player_damage_total=Player.power+player_dice_roll
                    Enemy.health-=player_damage_total
                    print(f"The {Enemy.name} attacks you for {enemy_damage_total} damage. Your health is {Player.health}")
                    print(f"You attack the {Enemy.name} and deal {player_damage_total} damage. The {Enemy.name} health is {Enemy.health}")
                    
                    if Player.health<=0:
                        events.death(Player)

                    if  Enemy.health<=0:
                        print(f"You win the fight against the {Enemy.name}")
                        Player.exp+=Enemy.exp
                        Player.gold+=Enemy.gold
                        print(f"You gain {Enemy.gold} gold ")
                        events.check_level_up(Player)
                        input("Press enter to continue")
                        battle=False
                        break
                    
                    input("Press any key to continue")
                    print("\033c", end="")
                    break
            
                 if choice in {b'e', b'E'}:
                
                     escape_chance= random.random()
                     if escape_chance < .40:
                         print("You manage to escape")
                         input("Press enter to continue")
                         battle=False
                         break
                     
                     else:
                         print ("You do not escape")
                         enemy_dice_roll=random.randint(1,12)
                         enemy_damage_total=max(0,Enemy.power+enemy_dice_roll)
                         Player.health-=enemy_damage_total
                         print(f"The {Enemy.name} attacks you for {enemy_damage_total} damage. Your health is {Player.health}")
                         input("Press any key to continue")
                         print("\033c", end="")

                         if Player.health<=0:
                             events.death(Player)
                     
                     break
        
        print("\033c", end="")
        maps.display_map(maps.visual_map_choice) 
                    

        

                      
         
          
      