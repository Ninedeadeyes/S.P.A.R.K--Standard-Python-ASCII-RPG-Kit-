
class Enemy():    
    def __init__(self,name,power,health,exp,gold):
        self.name=name
        self.power=power
        self.health=health
        self.exp=exp
        self.gold=gold

#Random Event enemies 

class Monster1  (Enemy):
    def __init__(self,name="Monster1",power=4,health=30,exp=5,gold=25):
        Enemy.__init__(self,name,power,health,exp,gold)

class Monster2  (Enemy):
    def __init__(self,name="Monster2",power=5,health=40,exp=7,gold=30):
        Enemy.__init__(self,name,power,health,exp,gold)

class Monster3 (Enemy):
    def __init__(self,name="Monster3",power=6,health=50,exp=10,gold=35):
        Enemy.__init__(self,name,power,health,exp,gold)
