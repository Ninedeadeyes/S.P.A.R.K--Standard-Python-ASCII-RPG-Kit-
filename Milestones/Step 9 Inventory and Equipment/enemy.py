
class Enemy():    
    def __init__(self,name,power,health,exp,gold):
        self.name=name
        self.power=power
        self.health=health
        self.exp=exp
        self.gold=gold

#Random Event enemies 

class Ghoul  (Enemy):
    def __init__(self,name="Ghoul",power=3,health=10,exp=5,gold=25):
        Enemy.__init__(self,name,power,health,exp,gold)

class BogImp  (Enemy):
    def __init__(self,name="Bog Imp",power=4,health=20,exp=7,gold=30):
        Enemy.__init__(self,name,power,health,exp,gold)

class RagMan (Enemy):
    def __init__(self,name="Rag man",power=5,health=30,exp=10,gold=35):
        Enemy.__init__(self,name,power,health,exp,gold)
