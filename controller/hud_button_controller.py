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
            pos_sprite_to_modify -- final position of the sprite where a route will be created
        """
        beginning = self.hud.level.level_controller.get_sprite_nearest("landsRoad", final_pos_sprite_to_modify)
        print(beginning)

        if final_pos_sprite_to_modify[0] < self.hud.level.grid_length_x and final_pos_sprite_to_modify[0] > 0:
            if final_pos_sprite_to_modify[1] < self.hud.level.grid_length_y and final_pos_sprite_to_modify[1] > 0:
                final_level_tile_to_modify = self.hud.level.level[final_pos_sprite_to_modify[0]][final_pos_sprite_to_modify[1]]
                
                # water
                if final_level_tile_to_modify['type_tile'] != "landsWater" and final_level_tile_to_modify['tile'] != "landWater1":
                    # mountain
                    if final_level_tile_to_modify['type_tile'] != "landsMountain" and final_level_tile_to_modify['tile'] != "landMountain1":
                        final_level_tile_to_modify['type_tile'] = "landsRoad"
                        final_level_tile_to_modify['tile'] = "landRoad1"