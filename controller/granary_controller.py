class Granary_Controller:
    def __init__(self, granary, hud):
        self.granary = granary
        self.hud = hud
        self.tile_to_modify = self.hud.level.level[self.granary.x][self.granary.y]
        self.loader = self.get_tile_load()
        self.index_of_animation_loader = 152
        self.direction_of_loader = 0
    def place_granary(self):        
        self.tile_to_modify["tile"] = "granary141"
        self.tile_to_modify["type_tile"] = "buildings"
        self.loader["tile"] = "granary146"
        self.loader["type_tile"] = "buildings"

    def animation_of_loader(self):
        self.loader["tile"] = "granary" + str(self.index_of_animation_loader)
        
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
        #self.loader["tile"] = "granary146"
        #self.loader["type_tile"] = "buildings"

    def get_tile_load(self):
        return self.hud.level.level[self.granary.x][self.granary.y+1]
    
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

