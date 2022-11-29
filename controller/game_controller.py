import pygame as pg
import sys

from controller.camera_controller import CameraController
from controller.hud_button_controller import HUDButtonController
from view.button import Button

class GameController:
    def __init__(self, game):
        self.game = game
        self.hud_btn_controller = HUDButtonController(self.game.level.hud)

    def run(self):
        self.playing = True

        while self.playing:
            self.game.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # controllers
        level_controller = self.game.level.level_controller
        camera_controller = CameraController(self.game.camera)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for btn in self.buttons:
                        if btn.rect.collidepoint(event.pos):
                            x, y = pg.mouse.get_pos()
                            grid_coords = level_controller.mouse_to_grid(x, y, camera_controller.camera.scroll)
                        
                            btn.ftn_click(grid_coords)
            
        self.buttons = []

        self.buttons.append(Button(pg.Rect(1219, 299, 40, 30), "", self.hud_btn_controller.create_road))

    def update(self):
        camera_controller = CameraController(self.game.camera)

        camera_controller.update()

    def draw(self):
        self.game.screen.fill((0, 0, 0))
        # level
        self.game.level.draw(self.game.screen, self.game.camera)
        # HUD
        self.game.level.hud.display_hud()

        for btn in self.buttons:
            self.hud_btn_controller.hover(btn)

        pg.display.flip()