class Weapon():    
    def __init__(self,name,damage):
        self.name=name
        self.damage=damage

    def __str__(self):
        return self.name     # This is needed so it reads the 'print' name not the memory eg : <weapon.WarHammer object at 0x00000235FA8FEBD0>
  
class Dagger  (Weapon):
    def __init__(self,name="Dagger",damage=2):
        Weapon.__init__(self,name,damage)

class Sword (Weapon):
    def __init__(self,name="Sword",damage=4):
        Weapon.__init__(self,name,damage)

    def __str__(self):
            return self.name

 