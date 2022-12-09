from random import random


class EngineerPost_Controller:
    def __init__(self,engineerPost,hud):
        self.engineerPost = engineerPost
        self.hud = hud
        self.tile_to_modify = self.hud.level.level[self.engineerPost.x][self.engineerPost.y]
    def place_post(self): 
        self.tile_to_modify["tile"] = "engineerPost"
        self.tile_to_modify["type_tile"] = "buildings"