from controller.hud_button_controller import HUDButtonController

class HUD():
    def __init__(self, level):
        self.level = level

    def display_hud(self):
        # controller
        hud_btn_controller = HUDButtonController(self, self.level)

        hud_btn_controller.create_route()