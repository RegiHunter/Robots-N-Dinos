from robot import Robot
from weapon import Weapon

class Fleet:

    def __init__(self) :
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        ww_cannon =  Weapon("Wild Wall-E Cannon", 60)
        orbital_strike = Weapon("Rapid-Fire Orbital strike", 80)
        gat_gun = Weapon("Mega Gatling Gun", 70)
        walle = Robot("Wall-E", ww_cannon)
        ultron = Robot("Ultron", orbital_strike )
        optimus = Robot("Opimus Prime", gat_gun)

        self.robots.append(walle)
        self.robots.append(ultron)
        self.robots.append(optimus)






    