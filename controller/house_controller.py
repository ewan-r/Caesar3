class HouseController():
    def __init__(self,House,hud):
        self.house = House
        self.hud = hud
    def place_house(self):
        tile_to_modify = self.hud.level.level[self.house.x][self.house.y]
        tile_to_modify["tile"] = "house1"
        tile_to_modify["type_tile"] = "houses"