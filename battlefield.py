from herd import Herd
from fleet import Fleet
from dino import Dino 
from robot import Robot

class Battlefield:
    def __init__(self):
        self.Robots = Fleet()
        self.Dinos = Herd()

    def run_game(self):
        pass
    def display_welcom(self):
        pass
    def battle(self):
        battle = [Dino.attack(Robot), Robot.attack(Dino)]
        conclusion = print(battle)
        return conclusion

While (Battlefield.battle())
    if Dino.health == 0 :
            win1 = print("Robots Win!")
            return win1
        
    elif Robot.health == 0 :
            win2 = print("Dinosaurs Win!")
            return win2
        
        

            
    def dino_turn(self, Dino):
        pass
    def robo_turn(self, Robot):
        pass
    def show_dino_opponent_options(self):
        pass
    def show_robo_opponent_options(self):
        pass
    def display_winners(self):
        pass


    