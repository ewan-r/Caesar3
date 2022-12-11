from model.farm import Farm
from controller.utils import *
import random
class Farm_Controller():
    def __init__(self,hud,farm, game):
        self.farm = farm
        self.hud = hud
        self.tile_to_modify = self.hud.level.level[self.farm.x][self.farm.y]
        self.neighbors = self.get_neighbors()
        self.area_to_plant = self.get_fertile_area()
        self.current_index_growing = 0
        self.workers = 0
        self.is_delivering = False
        self.can_grow = False
        self.game = game
        self.walker_controller = self.hud.level.walker_controller

    def place_farm (self):
        self.tile_to_modify["tile"] = "farm12"
        self.tile_to_modify["type_tile"] = "buildings"
        for tile in self.area_to_plant["area_to_modify"]:
            tile["tile"] = "farm13"
            tile["type_tile"] = "buildings"
        for tile in self.get_neighbors():
            tile["attached_to_building"] = self

    def destroy (self):
        for tile in self.get_neighbors:
            tile["tile"] = "landFarm1"
            tile["type_tile"] = "lands"
            tile["attached_to_building"] = []
        self.game.game.level.level_controller.economy_buildings.remove(self)
        self.game.game.level.level_controller.employers_buildings.remove(self)
    def update(self):

        if (self.workers > 0):
            if self.current_index_growing <= 4:
                if self.area_to_plant["status"][self.current_index_growing] < 17:
                    self.area_to_plant["status"][self.current_index_growing] += 1
                    self.grow_tile()
                else:
                    self.current_index_growing += 1
            else:
                self.deliver_wheat()
                if self.can_grow:
                    self.current_index_growing = 0
                    self.reset_farm()

    def reset_deliver (self):
        self.is_delivering = False

    def deliver_wheat (self):
        self.can_grow = False
        if not self.is_delivering:
            granaries = self.game.game.level.level_controller.granaries
            if len (granaries) > 0:
                granary = random.choice(granaries)
                neighbors = get_real_neighbors(granary.tile_to_modify, "road", self.hud.level.level)
                neighbor = None
                if (len(neighbors) > 0):
                    neighbor = random.choice(neighbors)
                    neighbors_departure = get_real_neighbors(self.hud.level.level[self.farm.x - 1][self.farm.y - 1],"road", self.hud.level.level)
                    neighbor_departure = None
                    if len(neighbors_departure) > 0:
                        neighbor_departure = random.choice(neighbors_departure)
                        self.walker_controller.new_walker(neighbor["grid"],self,3,neighbor_departure["grid"][0], neighbor_departure["grid"][1],self.hud.level.tiles["walkers"]["walker2"],granary, neighbor_departure["grid"])
                        self.can_grow = True
                        self.is_delivering = True

    def reset_farm (self):
        for x in range (len(self.area_to_plant["status"])):
                self.area_to_plant["status"][x] = 13
        for tile in self.area_to_plant["area_to_modify"]:
            tile["tile"] = "farm13"

    def grow_tile(self):

        farmnumber = self.area_to_plant["status"][self.current_index_growing]
        self.area_to_plant["area_to_modify"][self.current_index_growing]["tile"] = "farm"+str(farmnumber)

    def get_neighbors(self):
        neighbors = []
        #In order to link these tiles to this controller so when we delete one of these tiles we delete
        #The whole building
        for x in range (self.farm.x + 1,self.farm.x - 2,-1):
            for y in range (self.farm.y + 1, self.farm.y -2,-1):
                neighbors.append(self.hud.level.level[x][y])
        return neighbors

    def get_fertile_area(self):
        area_to_modify = []
        for x in range (self.farm.x-1, self.farm.x + 2):
            if x <= self.farm.x:
                area_to_modify.append(self.hud.level.level[x][self.farm.y+1])
            else:
                for y in range (self.farm.y+1, self.farm.y-2,-1):
                    area_to_modify.append(self.hud.level.level[x][y])
        out = {
            "area_to_modify" : area_to_modify,
            "status": [13 for x in area_to_modify]
        }
        return out