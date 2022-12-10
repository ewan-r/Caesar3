import random
from controller.utils import *

class EngineerPost_Controller:
    def __init__(self,engineerPost,hud):
        self.engineerPost = engineerPost
        self.hud = hud
        self.tile_to_modify = self.hud.level.level[self.engineerPost.x][self.engineerPost.y]
        self.walker_controller = self.hud.level.walker_controller
    def place_post(self): 
        self.tile_to_modify["tile"] = "engineerPost"
        self.tile_to_modify["type_tile"] = "buildings"
        self.create_engineer()
    
    def detect_and_repare_buldings(self, walker):
        area_of_detection = [(walker[3]+i,walker[4]+j) for i in range (-1,2) for j in range (-1,2)]
        for coords in area_of_detection:
            x = coords[0]
            y = coords[1]
            try :
                self.hud.level.level[x][y]["collapsed_counter"] = 0
                print(self.hud.level.level[x][y])
            except:
                pass


    def create_engineer (self):
        neighbors = get_real_neighbors(self.tile_to_modify, "road", self.hud.level.level)
        neighbor = None
        if (len(neighbors) > 0):
            neighbor = random.choice(neighbors)
        if (self.engineerPost.workers >= 1 and neighbor):
             self.walker_controller.new_walker(neighbor["grid"], self,2,neighbor["grid"][0], neighbor["grid"][1])
