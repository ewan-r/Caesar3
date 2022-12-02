class Reservoir_Controller:
    def __init__ (self,hud,reservoir):
        self.hud = hud
        self.reservoir = reservoir
        self.tile_to_modify = self.hud.level.level[reservoir.x][reservoir.y]
        self.water_placement = self.hud.level.level[reservoir.x-2][reservoir.y - 3]
        self.is_there_water = False
        self.index_of_animation = 35
    def place_reservoir (self):
        self.tile_to_modify["tile"] = "reservoir34"
        self.tile_to_modify["type_tile"] = "buildings"
        if (self.is_There_Water()):
            self.reservoir.status = "full"

    def is_There_Water(self):
        for x in range (self.reservoir.x - 5, self.reservoir.x + 5):
            for y in range (self.reservoir.y - 5, self.reservoir.y+5):
                if (self.hud.level.level[x][y]["type_tile"] == "landsWater" ):
                    return True
        return False
    def update_tile_water(self):
        self.water_placement["tile"] = "reservoir"+str(self.index_of_animation)
        self.water_placement["type_tile"] = "buildings"
    def update(self):
        if (self.reservoir.status == "full"):
            if (self.index_of_animation < 42):
                self.update_tile_water()
                self.index_of_animation +=1
            else:
                self.index_of_animation = 35
            #We change tile in reservoir in order to display that it is full
            #self.water_placement["tile"] = "reservoir35"
            #self.water_placement["type_tile"] = "buildings"
            #It works but we need to blit it after the reservoir in order to display over the reservoir