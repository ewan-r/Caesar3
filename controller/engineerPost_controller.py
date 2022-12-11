import random
from controller.utils import *

class EngineerPost_Controller:
    def __init__(self,engineerPost,hud, game):
        self.engineerPost = engineerPost
        self.hud = hud
        self.tile_to_modify = self.hud.level.level[self.engineerPost.x][self.engineerPost.y]
        self.game = game
        self.walker_controller = self.hud.level.walker_controller
        self.workers = self.engineerPost.workers
        self.isEngineerOut = False
    
    def destroy (self):

        self.tile_to_modify["tile"] = ""
        self.tile_to_modify["type_tile"] = ""
        self.tile_to_modify["attached_to_building"] = []
        self.game.level.level_controller.buildings.remove(self)
        self.game.level.level_controller.employers_buildings.remove(self)


    def place_post(self): 
        self.tile_to_modify["tile"] = "engineerPost"
        self.tile_to_modify["type_tile"] = "buildings"
        self.tile_to_modify["attached_to_building"] = self
        self.create_engineer()
    
    def update(self, buildings):
        self.create_engineer()

    def detect_and_repare_buldings(self, walker):
        area_of_detection = [(walker[3]+i,walker[4]+j) for i in range (-1,2) for j in range (-1,2)]
        for coords in area_of_detection:
            x = coords[0]
            y = coords[1]
            try :
                self.hud.level.level[x][y]["collapsed_counter"] = 0
            except:
                pass


    def create_engineer (self):
        if not self.isEngineerOut:
            neighbors = get_real_neighbors(self.tile_to_modify, "road", self.hud.level.level)
            neighbor = None
            #print(self.workers)
            if (len(neighbors) > 0):
                neighbor = random.choice(neighbors)
            if (self.workers >= 1 and neighbor):
                self.walker_controller.new_walker(neighbor["grid"], self,2,neighbor["grid"][0], neighbor["grid"][1],self.hud.level.tiles["walkers"]["walker1"])
                self.isEngineerOut = True