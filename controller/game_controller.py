import pygame as pg
import sys

from controller.camera_controller import CameraController

class GameController:
    def __init__(self, game):
        self.game = game

    def run(self):
        self.playing = True
        while self.playing:
            self.game.clock.tick(60)
            self.events()
            self.update()
            self.draw()
            self.position_mouse_grid()
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
        camera_controller = CameraController(self.game.camera)
        
        camera_controller.update()

    def draw(self):
        self.game.screen.fill((0, 0, 0))
        self.game.level.draw(self.game.screen, self.game.camera)

        pg.display.flip()

    def position_mouse_grid(self):
        x, y = pg.mouse.get_pos()
        level_controller = self.game.level.level_controller

        # detect roads
        level_controller.mouse_on_sprite(level_controller.mouse_to_grid(x, y), level_controller.get_list_pos_sprites('landsRoad'))