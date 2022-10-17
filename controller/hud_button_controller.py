class HUDButtonController():
    """A HUDButtonController."""  

    def __init__(self, hud, level):
        """HUDButtonController constructor.
        
        Argument:
            menu -- menu to be updated
        """
        self.hud = hud
        self.level = level

    def create_route(self):
        """Create a route"""

        print(self.level.level_controller.get_list_pos_sprites('landsRoad'))