import random
from controller.utils import *

class HouseController():
    def __init__(self,House,hud):
        self.house = House
        self.hud = hud
        self.tile_to_modify = self.hud.level.level[self.house.x][self.house.y]
        self.level = self.hud.level.level
        self.walker_controller = self.hud.level.walker_controller
    def place_house(self):
        
        self.tile_to_modify["tile"] = "house1"
        self.tile_to_modify["type_tile"] = "buildings"
        self.call_migrant()
        #Il faut modifier l'appel à new walker pour que les walkers ne soient pas génés par le manque de route

    def call_migrant (self):
        neighbors = get_real_neighbors(self.tile_to_modify, "road", self.level)
        neighbor = None
        if (len(neighbors) > 0):
            neighbor = random.choice(neighbors)
        if(neighbor):
            self.walker_controller.new_walker(neighbor["grid"])


    def collapse_counter_increase(self):
        IncreaseCounter = random.randint(1,100)
        if IncreaseCounter < 2:
            self.house.collapseCounter += 1
        
    def update(self):
        if self.house.collapseCounter >= 10:
            self.tile_to_modify['tile'] = "ruin"
            self.house.state = "collapsed"
        else:
            self.collapse_counter_increase()