class Dino :
    

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def raptor(self):
        self.name = "Utah Raptor"
        self.health = 2000
        self.attack_power = 1000


    def trex(self):
        self.name = "Tyrannosaurus"
        self.health = 3000
        self.attack_power = 800

        
    def Giga(self):
        self.name = "Giganotosaurus"
        self.health = 7000
        self.attack_power = 600