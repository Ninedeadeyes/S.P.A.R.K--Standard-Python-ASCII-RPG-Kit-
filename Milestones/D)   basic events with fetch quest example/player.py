


class Player(object):
    def __init__ (self,health,gold,power,x,y):
        self.inventory=["Spell book"]
        self.armour=("Leather Armour")
        self.weapon=("Knife")
        self.health=health
        self.gold=gold
        self.power=power
        self.x=x
        self.y=y
        self.spoon_quest=False 
        self.got_spoon_for_quest=False