from herd import Herd
from weapon import Weapon
from herd import Herd
from dino import Dino 

class Robot:

    def __init__(self, name, weapon):
        self.name = name
        self.health = 200
        self.weapon = weapon

    def attack(self):
        health = Dino.health()
        atk = Weapon.attack_power()
        new_health = health - atk
        return new_health

        