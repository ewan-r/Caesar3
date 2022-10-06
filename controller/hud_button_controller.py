class HUDButtonController():
    """A HUDButtonController."""  

    def __init__(self, hud, level_controller):
        """HUDButtonController constructor.
        
        Argument:
            menu -- menu to be updated
        """
        self.hud = hud
        self.level_controller = level_controller

    def create_route(self):
        """Create a route"""

        print(self.level_controller.get_pos_sprites('landsRoad'))