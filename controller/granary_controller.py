from controller.utils import * 

class Granary_Controller:
    def __init__(self, granary, hud, game):
        self.granary = granary
        self.hud = hud
        self.tile_to_modify = self.hud.level.level[self.granary.x][self.granary.y]
        self.loader = self.get_tile_load()
        self.neighbors = self.get_neighbors_tiles()
        self.game = game
        self.index_of_animation_loader = 152
        self.direction_of_loader = 0
        self.walker_controller = self.hud.level.walker_controller
    def place_granary(self):        
        self.tile_to_modify["tile"] = "granary141"
        self.tile_to_modify["type_tile"] = "buildings"
        self.loader["tile"] = "granary146"
        self.loader["type_tile"] = "buildings"
        self.game.game.level.level_controller.granaries.append(self)
        for tile in self.get_neighbors_tiles():
            #tile["attached_to_building"] = self
            tile["destructible"] = True

    def destroy (self):
        for tile in self.get_neighbors_tiles():
            print("Tile bfore:")
            print(tile)
            tile["tile"] = ""
            tile["type_tile"] = ""
            tile["attached_to_building"] = []
            print("Tile after :")
            print(tile)
        self.game.game.level.level_controller.granaries.remove(self)
        self.game.game.level.level_controller.economy_buildings.remove(self)

    def receipt_wheat(self, arrival, departure, farm):
        self.game.food += 100
        self.walker_controller.new_walker(arrival, farm, 4, departure[0], departure[1],self.hud.level.tiles["walkers"]["walker2"])
   
   
    def animation_of_loader(self):
        self.loader["tile"] = "granary" + str(self.index_of_animation_loader)
        
    def get_neighbors_tiles (self):
        neighbors = []
        for x in range (self.granary.x,self.granary.x - 3,-1):
            for y in range (self.granary.y, self.granary.y + 3):
                neighbors.append(self.hud.level.level[x][y])
        return neighbors
    def update (self):
        if (self.direction_of_loader == 0):
            if (self.index_of_animation_loader < 152):
                self.index_of_animation_loader += 1
            else:
                self.direction_of_loader = 1
        else:
            if (self.index_of_animation_loader > 146):
                self.index_of_animation_loader -= 1
            else:
                self.direction_of_loader = 0
        self.animation_of_loader()

    def get_tile_load(self):
        return self.hud.level.level[self.granary.x][self.granary.y+2]
    
    def deliver_wheat(self, amount_to_deliver):
        #This function aims to be activated by the walker to deliver the wheat in granary
        self.granary.stock_wheat += amount_to_deliver
        if self.granary.stock_wheat > 250:
            #Change a tile in order to display that we reached a stage
            pass
        elif self.granary.stock_wheat > 500:
            #Change another tile
            pass
        elif self.granary.stock_wheat > 750:
            #Another one
            pass


