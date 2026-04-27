
class Enemy():    
    def __init__(self,name,power,health,experience,gold):
        self.name=name
        self.power=power
        self.health=health
        self.experience=experience
        self.gold=gold

#Random Event enemies 

class Ghoul  (Enemy):
    def __init__(self,name="Ghoul",power=15,health=185,experience=10,gold=25):
        Enemy.__init__(self,name,power,health,experience,gold)

class BogImp  (Enemy):
    def __init__(self,name="Bog Imp",power=2,health=20,experience=30,gold=30):
        Enemy.__init__(self,name,power,health,experience,gold)

class RagMan (Enemy):
    def __init__(self,name="Rag man",power=4,health=25,experience=40,gold=35):
        Enemy.__init__(self,name,power,health,experience,gold)
