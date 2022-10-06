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