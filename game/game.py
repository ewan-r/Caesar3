from .world import World
from .settings import TILE_SIZEX, TILE_SIZEY
import pygame as pg
import sys



class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.world = World(100 , 100, self.width, self.height)

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

    def update(self):
        pass

    def draw(self):
        
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.world.grass_lands, (0,0))

        for x in range(self.world.grid_length_x):

            for y in range(self.world.grid_length_y):

                sq = self.world.world[x][y]["cart_rect"]
                rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZEX, TILE_SIZEY)
                #pg.draw.rect(self.screen, (0, 0, 255), rect, 1)

                render_pos = self.world.world[x][y]["render_pos"]

                self.screen.blit(self.world.tiles["grass_land"], (render_pos[0] + self.width/2, render_pos[1] + self.height/4))

                tile = self.world.world[x][y]["tile"]

                if tile != "":
                    self.screen.blit(self.world.tiles[tile],(render_pos[0] + self.width/2, render_pos[1] + self.height/4 - (self.world.tiles[tile].get_height() - TILE_SIZEY)))

                p = self.world.world[x][y]["iso_poly"]
                p = [(x + self.width/2, y + self.height/4) for x, y in p]
                pg.draw.polygon(self.screen, (255, 0, 0), p, 1)


        pg.display.flip()