from robot import Robot
from weapon import Weapon
from fleet import Fleet

class Dino:
    

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 300
        self.attack_power = attack_power

    def attack(self, Robot):
        health = Fleet.Robot.health()
        atk = Weapon.attack_power()
        new_health = health - atk
        return new_health

   