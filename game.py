import pygame as pg
import sys
from camera import Camera
from level import Level

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.entities = []

        self.level = Level(self.entities, 40, 40, self.width, self.height)

        # camera
        self.camera = Camera(self.width, self.height)


    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
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
                    sys.exit()

    def update(self):
        self.camera.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.level.draw(self.screen, self.camera)


        pg.display.flip()