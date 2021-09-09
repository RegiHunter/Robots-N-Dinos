from weapon import Weapon

class Robot :

    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

        

    def wall_e(self):
        self.name = "Wall-E"
        self.health = 1500
        self.weapon = Weapon("Wild Wall-E Cannon", 1000)

    def ultron(self):
        self.name = "Ultron"
        self.health = 6000
        self.weapon = Weapon("Rapid-Fire Orbital Strikes"800)

    def optimus(self):
        self.name = "Optimus"
        self.health = 4000
        self.weapon = Weapon("Mega Gatling Gun", 400)