from model.farm import Farm


class Farm_Controller():
    def __init__(self,hud,farm):
        self.farm = farm
        self.hud = hud
        self.tile_to_modify = self.hud.level.level[self.farm.x][self.farm.y]
        self.neighbors = self.get_neighbors()
        self.area_to_plant = self.get_fertile_area()
        self.current_index_growing = 0

    def place_farm (self):
        self.tile_to_modify["tile"] = "farm12"
        self.tile_to_modify["type_tile"] = "buildings"
        for tile in self.area_to_plant["area_to_modify"]:
            tile["tile"] = "farm13"
            tile["type_tile"] = "buildings"

    def update(self):

        if self.current_index_growing <= 4:
            if self.area_to_plant["status"][self.current_index_growing] < 17:
                self.area_to_plant["status"][self.current_index_growing] += 1
                self.grow_tile()
            else:
                self.current_index_growing += 1
        else:
            self.current_index_growing = 0
            self.reset_farm()
            
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
        for x in range (self.farm.x,self.farm.x + 4 ):
            for y in range (self.farm.y, self.farm.y + 4):
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