import random
import msvcrt
import battle
import enemy


nothing_list=["You look for deadly traps but find none","You find nothing of interest here, maybe next time", "Wait..You hear something..It must be your imagination",          
             " You find nothing of interest here"]


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
    


#QUEST 

def spoon_found(Player):
  
    print("You find a spoon on the floor do you pick it up (Y or N) ?")

    while True:        # ignores all non instruction keypress 
    
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You pick up the spoon")
            Player.got_spoon_for_quest=True
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide to leave it")
            
            return False



def goblin_spoon_quest(Player):

    if Player.got_spoon_for_quest==False and Player.spoon_quest==False:
        print("Have you seen my spoon ?")
    
    elif Player.got_spoon_for_quest==True and Player.spoon_quest==False:
            print("You have found my spoon, thank you !!")
            Player.spoon_quest=True
    else:
        print("Spoon, spoon I love my spoon la la la laaaaaa ")

