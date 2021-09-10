from dino import Dino
 

class Herd:


    def __init__(self):
        self.dinos = []
        self.create_herd()

    def create_herd(self):
        raptor = Dino("Utah Raptor", 40)
        trex = Dino("Tyrannosaurus", 60)
        giga = Dino("Giganotosaurus", 50)

        self.dinos.append(raptor)
        self.dinos.append(trex)
        self.dinos.append(giga)

