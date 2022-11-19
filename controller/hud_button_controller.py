class HUDButtonController():
    """A HUDButtonController."""  

    def __init__(self, hud):
        """HUDButtonController constructor.
        
        Argument:
            hud -- HUD to be updated
        """
        self.hud = hud

    def create_road(self, final_pos_sprite_to_modify):
        """Create a road.
        
        Argument:
            final_pos_sprite_to_modify -- final position of the sprite where a route will be created
        """
        beginning = self.hud.level.level_controller.get_sprite_nearest("landsRoad", final_pos_sprite_to_modify)

        direction = None

        if (final_pos_sprite_to_modify[0] < beginning[0]):
            direction = "up"
        elif (final_pos_sprite_to_modify[0] > beginning[0]):
            direction = "down"
        elif (final_pos_sprite_to_modify[1] < beginning[1]):
            direction = "right"
        elif (final_pos_sprite_to_modify[1] > beginning[1]):
            direction = "left"

        list_tiles_to_modify = self.hud.level.level_controller.get_list_tiles_to_modify(direction, beginning, final_pos_sprite_to_modify)       

        if final_pos_sprite_to_modify[0] < self.hud.level.grid_length_x and final_pos_sprite_to_modify[0] >= 0:
            if final_pos_sprite_to_modify[1] < self.hud.level.grid_length_y and final_pos_sprite_to_modify[1] >= 0:
                for tile in list_tiles_to_modify:
                    tile_to_modify = self.hud.level.level[tile[0]][tile[1]]
                    
                    # water
                    if tile_to_modify['type_tile'] != "landsWater" and tile_to_modify['tile'] != "landWater1":
                        # mountain
                        if tile_to_modify['type_tile'] != "landsMountain" and tile_to_modify['tile'] != "landMountain1":
                            # tree
                            if tile_to_modify['type_tile'] != "landsForests" and tile_to_modify['tile'] != "landForest45":
                                tile_to_modify['type_tile'] = "landsRoad"
                                tile_to_modify['tile'] = "landRoad1"