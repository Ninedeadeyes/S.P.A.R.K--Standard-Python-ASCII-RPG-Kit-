
class Enemy():    
    def __init__(self,name,power,health,exp,gold):
        self.name=name
        self.power=power
        self.health=health
        self.exp=exp
        self.gold=gold

#Random Event enemies 

class Ratling  (Enemy):
    def __init__(self,name="Ratling",power=4,health=30,exp=5,gold=25):
        Enemy.__init__(self,name,power,health,exp,gold)

class BogImp  (Enemy):
    def __init__(self,name="Bog Imp",power=5,health=40,exp=7,gold=30):
        Enemy.__init__(self,name,power,health,exp,gold)

class Hobgoblin (Enemy):
    def __init__(self,name="HobGoblin",power=6,health=50,exp=10,gold=35):
        Enemy.__init__(self,name,power,health,exp,gold)
