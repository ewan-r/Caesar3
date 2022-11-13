class HUDButtonController():
    """A HUDButtonController."""  

    def __init__(self, hud):
        """HUDButtonController constructor.
        
        Argument:
            hud -- HUD to be updated
        """
        self.hud = hud

    def create_road(self, pos_sprite_to_modify):
        """Create a road.
        
        Argument:
            pos_sprite_to_modify -- position of the sprite where a route will be created
        """

        level_tile_to_modify = self.hud.level.level[pos_sprite_to_modify[0]][pos_sprite_to_modify[1]]
        
        level_tile_to_modify['type_tile'] = "landsRoad"
        level_tile_to_modify['tile'] = "landRoad1"