class HUDButtonController():
    """A HUDButtonController."""  

    def __init__(self, hud):
        """HUDButtonController constructor.
        
        Argument:
            hud -- HUD to be updated
        """
        self.hud = hud

    def create_road(self, grid_coords):
        """Create a road.
        
        Argument:

        """
        if grid_coords[0] < self.hud.level.grid_length_x and grid_coords[1] < self.hud.level.grid_length_y:
            if grid_coords[0] >= 0 and grid_coords[1] >= 0:
                tile_to_modify = self.hud.level.level[grid_coords[0]][grid_coords[1]]
                
                # water
                if tile_to_modify['type_tile'] != "landsWater":
                    # mountain
                    if tile_to_modify['type_tile'] != "landsMountain":
                        # forest
                        if tile_to_modify['type_tile'] != "landsForests":
                            # road
                            if tile_to_modify['type_tile'] != "landsRoad":
                                tile_to_modify['type_tile'] = "landsRoad"
                                
                                neighbors = self.hud.level.level_controller.get_neighbors(grid_coords)

                                if tile_to_modify['grid'][0] == self.hud.level.grid_length_x-1:
                                    tile_to_modify['tile'] = "landRoad3"
                                else:
                                    up = self.hud.level.level[grid_coords[0]+1][grid_coords[1]]
    
                                    # up
                                    if up in neighbors:
                                        tile_to_modify['tile'] = "landRoad2"
                                    # default
                                    else:
                                        tile_to_modify['tile'] = "landRoad3"