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
            
                if tile_to_modify['type_tile'] == "":
                    tile_to_modify['type_tile'] = "landsRoad"
                    
                    neighbors = self.hud.level.level_controller.get_neighbors(grid_coords)

                    if tile_to_modify['grid'][0] == self.hud.level.grid_length_x-1 or tile_to_modify['grid'][1] == self.hud.level.grid_length_y-1:
                        tile_to_modify['tile'] = "roadIntersection"
                    else:
                        up = self.hud.level.level[grid_coords[0]+1][grid_coords[1]]
                        down = self.hud.level.level[grid_coords[0]-1][grid_coords[1]]
                        right = self.hud.level.level[grid_coords[0]][grid_coords[1]+1]
                        left = self.hud.level.level[grid_coords[0]][grid_coords[1]-1]

                        # up
                        if up in neighbors:
                            if up['tile'] == "roadLeft":
                                up['tile'] = "roadUpNextToLeft"

                            if up['tile'] == "roadRight":
                                up['tile'] = "roadUpNextToRight"
                            
                            tile_to_modify['tile'] = "roadUp"
                        # down
                        elif down in neighbors:
                            if down['tile'] == "roadLeft":
                                down['tile'] = "roadDownNextToLeft"

                            if down['tile'] == "roadRight":
                                down['tile'] = "roadDownNextToRight"

                            tile_to_modify['tile'] = "roadDown"
                        # right
                        elif right in neighbors:
                            if right['tile'] == "roadUp":
                                right['tile'] = "roadRightNextToUp"

                            if right['tile'] == "roadDown":
                                right['tile'] = "roadRightNextToDown"
                            
                            tile_to_modify['tile'] = "roadRight"
                        # left
                        elif left in neighbors:
                            if left['tile'] == "roadUp":
                                left['tile'] = "roadLeftNextToUp"

                            if left['tile'] == "roadDown":
                                left['tile'] = "roadLeftNextToDown"

                            tile_to_modify['tile'] = "roadLeft"
                        # default
                        else:
                            tile_to_modify['tile'] = "roadIntersection"