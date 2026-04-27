import random
import msvcrt
import battle
import weapon
import armour
import enemy
import sys

nothing_list=["You look for deadly traps but find none","You find nothing of interest here, maybe next time", "Wait..You hear something..It must be your imagination",          
             " You find nothing of interest here"]

# progress events functions 

def win():
    print ("You win!")
    print("GAME OVER")
    input("Press enter to exit")
    sys.exit()


def death(Player):
    if Player.health<=0:
        print("Wounds upon wounds, you fall to your death ")
        print("GAME OVER")
        input("Press enter to exit")
        sys.exit()

def check_level_up(Player):
    if Player.exp>15*Player.level:
        Player.level+=1
        Player.exp=0
        print(f"You have gained a level. You are now level {Player.level}")
        print ("What would you like to increase Power(P) or Health(H) ?")

        while True:
            level_up_choice = msvcrt.getch()

            if level_up_choice in {b'p', b'P'}:
                power_increase=random.randint (2,4)
                Player.full_power+=power_increase
                Player.power=Player.full_power
                Player.health=Player.full_health
                print(f"You power has increased by {power_increase}")
                print (f"Your power is now {Player.power}.")
                break
            
            if level_up_choice in {b'h', b'H'}:
                health_increase=random.randint (20,30)
                Player.full_health+=health_increase
                Player.health=Player.full_health
                print(f"You power has increased by {health_increase}")
                print (f"Your health is now {Player.health}.")
                break
        
        Player.level+=1
        Player.exp=0

# random events function

def random_event(Player):

    r=random.random()
    
    if r < 0.85 :
        nothing_happened()

    elif r < 0.95:
        random_battle(Player)
                    
    else:
        loot(Player)            

def random_battle(Player):
    r= random.random()
    if r < .50:
        battle.fight(Player,enemy.Ghoul())

    elif r < .80:
        battle.fight(Player,enemy.BogImp())

    elif r<.90: 
        battle.fight(Player,enemy.RagMan())


def nothing_happened():
    noEvent=random.choice(nothing_list)
    print(noEvent)


def loot(Player):     #not needing an augement because 'return' was used. 
    gold_pickup=random.randint(1,12)
    if gold_pickup==1:
        Player.gold+=gold_pickup
        print(f"You find a {gold_pickup} gold coin on the floor")

    else:
        
        Player.gold+=gold_pickup
        print(f"You find {gold_pickup} gold coins on the floor")

# Quest events functions 

def spoon_found(Player):
  
    print("You find a spoon on the floor do you pick it up (Y or N) ?")

    while True:        # ignores all non instruction keypress 
    
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You pick up the spoon")
            Player.got_spoon_for_quest=True
            Player.inventory.append("Spoon")
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide to leave it")
            
            return False



def goblin_spoon_quest(Player):

    if Player.got_spoon_for_quest==False and Player.spoon_quest==False:
        print("Goblin: Have you seen my spoon ?")
    
    elif Player.got_spoon_for_quest==True and Player.spoon_quest==False:
            print("Goblin: You have found my spoon, thank you !!")
            print("Goblin: For your troubles, Here is a warhammer and a suit of leather armour")
            Player.inventory.remove("Spoon")
            Player.inventory.append(weapon.WarHammer())
            Player.inventory.append(armour.LeatherArmour())
            Player.spoon_quest=True
    else:
        print("Goblin: Spoon, spoon I love my spoon la la la laaaaaa ")
        print("Goblin: are you still here ? ")
        print("Goblin: You've beaten the game go home and be a family person")
        win()


