import pygame as pg
import sys

from controller.camera_controller import CameraController
from controller.hud_button_controller import HUDButtonController

class GameController:
    """A GameController."""

    def __init__(self, game):
        """GameController constructor.
        
        Argument:
            game -- game to control
        """
        self.game = game

    def run(self):
        """Run a game in a loop."""
        self.playing = True

        while self.playing:
            self.game.clock.tick(60)
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        """Activate features during a game."""
        # controllers
        level_controller = self.game.level.level_controller
        hud_btn_controller = HUDButtonController(self.game.level.hud)
        camera_controller = CameraController(self.game.camera)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

        x_pos_mouse, y_pos_mouse = pg.mouse.get_pos()
        pos_mouse = level_controller.mouse_to_grid(x_pos_mouse, y_pos_mouse, camera_controller.camera.scroll)

        if pg.mouse.get_pressed()[0]:
            click_x_pos_mouse, click_y_pos_mouse = pg.mouse.get_pos()
            click_pos = level_controller.mouse_to_grid(click_x_pos_mouse, click_y_pos_mouse, camera_controller.camera.scroll)          

            hud_btn_controller.create_road(click_pos, pos_mouse)

    def update(self):
        """Update a game."""
        camera_controller = CameraController(self.game.camera)
        
        camera_controller.update()

    def draw(self):
        """Draw sprites of a game."""
        self.game.screen.fill((0, 0, 0))
        self.game.level.draw(self.game.screen, self.game.camera)

        pg.display.flip()