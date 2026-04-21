class Armour():  
    def __init__(self,name,protection):
        self.name=name
        self.protection=protection

    def __str__(self):
        return self.name     # This is needed so it reads the 'print' name not the memory eg : <weapon.WarHammer object at 0x00000235FA8FEBD0>
    
class Rags(Armour):
    def __init__(self,name="Rags",protection=1):
        Armour.__init__(self,name,protection,)


class LeatherTunic(Armour):
    def __init__(self,name="Leather Tunic",protection=2):
        Armour.__init__(self,name,protection)

