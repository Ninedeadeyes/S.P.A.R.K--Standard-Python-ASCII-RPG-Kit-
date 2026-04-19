
import armour
import weapon
import msvcrt

def order(bag):
    for x in range(len(bag)): 
        print (x+1, str(bag[x]))


def play_instruction():
    print(" Instructions ")   
    print(" Movement: WASD, Inventory : I ")  

def commands(Player):
    print("                                   ")
    print("                                    ")
    print(f" Level:{Player.level} Health: {Player.health} Power: {Player.power} Gold: {Player.gold}")
    print(f" Armour: {Player.armour.name} + {Player.armour.protection} Protection   Weapon: {Player.weapon.name} + {Player.weapon.damage} Damage")

    while True:        # ignores all non instruction keypress 
        
            instruction = msvcrt.getch()

            if instruction in {b'w', b'W'}: # Up
                Player.y = Player.y-1
                break
                
            if instruction in {b's', b'S'}: # Down
                Player.y = Player.y+1
                break
        
            if instruction in {b'd', b'D'}: # Right
                Player.x = Player.x+1
                break
                
            if instruction in {b'a', b'A'}: # Left
                Player.x = Player.x-1
                break
            
            if instruction in {b'i', b'I'}: # Left
                print("Bag(B), Change(C), Exit(E)")

                while True:
            
                    instruction = msvcrt.getch()

                    if instruction in {b'b', b'B'}:
                         if Player.inventory==[""]:
                             print("Your bag is empty")
                        
                         else:
                             
                            order(Player.inventory)

                         print("Press E to Exit")
                         
                    
                    if instruction in {b'c', b'C'}:
                         print("Weapon (W), Armour(A), Exit(E)")

                         while True:
                              
                              instruction = msvcrt.getch()

                              if instruction in {b'w', b'W'}:
                                   
                                Weapons=[item for item in Player.inventory if isinstance (item,weapon.Weapon)]
                                
                                if not Weapons:
                                    print("You do not have any Weapon to equip")
                                    print("Press E for Exit")
                                    break

                                print (" Choose a Weapon to equip :")
                                

                                for i,item in enumerate(Weapons,1):

                                    print ("{}. {}".format(i,item))

                                valid=False
                                while not valid:
                                    choice=input("")
                                    try:
                                        old_weapon=Player.weapon # fix bug that replicate item if error 
                                        Player.inventory.remove(Weapons[int(choice)-1])
                                        Player.weapon=Weapons[int(choice)-1]
                                        Player.inventory.append(old_weapon)
                                        print("You arm yourself with :",Weapons[int(choice)-1])
                                        print("Press E for Exit")
                                        valid=True 
                                        break

                                    except (ValueError,IndexError):
                                        print("Invalid choice, try again ")
                                        
                                
                                break

                              if instruction in {b'a', b'A'}:

                                Armours=[item for item in Player.inventory if isinstance (item,armour.Armour)]
                                
                                if not Armours:
                                    print("You do not have any Armour to equip")
                                    print("Press E for Exit")
                                    break

                                print (" Choose an Armour to equip :")

                                for i,item in enumerate(Armours,1):

                                    print ("{}. {}".format(i,item))

                                valid=False
                                while not valid:
                                    choice=input("")
                                    try:
                                        old_armour=Player.armour # fix bug that replicate item if error 
                                        Player.inventory.remove(Armours[int(choice)-1])
                                        Player.armour=Armours[int(choice)-1]
                                        Player.inventory.append(old_armour)
                                        print("You equip yourself with:", Armours[int(choice)-1])
                                        print("Press E for Exit")
                                        valid=True 
                                        break

                                    except (ValueError,IndexError):
                                        print("Invalid choice, try again ")
                                
                                break



                              if instruction in {b'e', b'E'}:
                                   break

                    
                    if instruction in {b'e', b'E'}:
                        break

                break

