import pygame as pg
import sys

from controller.camera_controller import CameraController
from controller.hud_button_controller import HUDButtonController
from view.button import Button

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

        btn_clicked = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                btn_clicked = True

        x, y = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        grid_coords = level_controller.mouse_to_grid(x, y, camera_controller.camera.scroll)

        if click[0]:
            hud_btn_controller.create_road(grid_coords)

    def update(self):
        """Update a game."""
        camera_controller = CameraController(self.game.camera)

        camera_controller.update()

    def draw(self):
        """Draw sprites of a game."""
        self.game.screen.fill((0, 0, 0))
        # level
        self.game.level.draw(self.game.screen, self.game.camera)
        # HUD
        self.game.level.hud.display_hud()

        hud_btn_controller = HUDButtonController(self.game.level.hud)
        road_btn = Button(pg.Rect(1268, 299, 42, 29), "", hud_btn_controller.create_road)
        road_btn.hover(self.game.screen, road_btn) 

        pg.display.flip()