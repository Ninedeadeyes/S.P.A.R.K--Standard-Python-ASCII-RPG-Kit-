import weapon
import armour

class Player(object):
    def __init__ (self,level,exp,health,power,gold,x,y):
        self.alive=True
        self.inventory=["Bone Flute"]
        self.armour=armour.Rags()
        self.weapon=weapon.Dagger()
        self.level=level
        self.exp=exp
        self.health=health
        self.full_health=100
        self.power=power
        self.gold=gold
        self.full_power=12
        self.x=x
        self.y=y
        self.spoon_quest=False 
        self.got_spoon_for_quest=False

