import random
class HouseController():
    def __init__(self,House,hud):
        self.house = House
        self.hud = hud
        self.tile_to_modify = self.hud.level.level[self.house.x][self.house.y]
    def place_house(self):
        
        self.tile_to_modify["tile"] = "house1"
        self.tile_to_modify["type_tile"] = "buildings"

    def collapse_counter_increase(self):
        IncreaseCounter = random.randint(1,100)
        if IncreaseCounter < 2:
            self.house.collapseCounter += 1
        
    def update(self):
        if self.house.collapseCounter >= 10:
            self.tile_to_modify['tile'] = "ruin"
        else:
            self.collapse_counter_increase()