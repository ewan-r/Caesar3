import random
from controller.utils import *

class HouseController():
    def __init__(self,House,hud, game):
        self.house = House
        self.hud = hud
        self.time = 0
        self.tile_to_modify = self.hud.level.level[self.house.x][self.house.y]
        self.level = self.hud.level.level
        self.walker_controller = self.hud.level.walker_controller
        self.game = game

    def place_house(self):    
        self.tile_to_modify["tile"] = "house0"
        self.tile_to_modify["type_tile"] = "buildings"
        self.tile_to_modify["attached_to_building"] = self
        self.call_migrant()
        self.tile_to_modify["destructible"] = True
        #Il faut modifier l'appel à new walker pour que les walkers ne soient pas génés par le manque de route

    def destroy(self):
        self.tile_to_modify["tile"] = ""
        self.tile_to_modify["type_tile"] = ""
        self.tile_to_modify["attached_to_building"] = []
        self.game.game.level.level_controller.buildings.remove(self)
        self.game.citizens -= self.house.citizens


    def call_migrant (self):
        neighbors = get_real_neighbors(self.tile_to_modify, "road", self.level)
        neighbor = None
        if (len(neighbors) > 0):
            neighbor = random.choice(neighbors)
        if(neighbor):
            self.walker_controller.new_walker(neighbor["grid"], self)


    def collapse_counter_increase(self):
        IncreaseCounter = random.randint(1,100)
        if IncreaseCounter < 2 and self.house.level != 0:
            self.tile_to_modify["collapsed_counter"] += 1
            self.house.collapseCounter = self.tile_to_modify["collapsed_counter"]
    
    def upgrade(self):
        self.house.level += 1

        self.house.citizens += 2
        self.house.max_citizens += 2
        self.game.citizens += 2
        self.tile_to_modify["tile"] = "house"+str(self.house.level)

    def update(self, buildings):
        if self.tile_to_modify["collapsed_counter"] >= 10:
            self.tile_to_modify['tile'] = "ruin"
            self.house.state = "collapsed"
            self.game.citizens -= self.house.citizens 
            buildings.remove(self)
        else:
            self.collapse_counter_increase()
            if (self.time == 500):
                if (self.game.food - 10 * self.house.citizens  > 0):
                    self.game.food -= 10 * self.house.citizens
                    if (self.house.citizens < self.house.max_citizens):
                        self.house.citizens += 1
                        self.game.citizens += 1
                else :
                    self.house.citizens -= 1
                    self.game.citizens -=1
                self.time = 0
            else : 
                self.time += 1