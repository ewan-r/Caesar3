import pygame as pg
from pygame.locals import *
from view.input_field import TextField
from view.button import Button


class FilterMenu():

    def __init__(self, window, background_image,level):
        self.window = window
        self.background = background_image
        self.level = level
        self.buttons = []

    def display_menu(self, grid_coord):
        """Display the game menu."""
        level_tile_to_modify = self.level.level[grid_coord[0]][grid_coord[1]]
        if level_tile_to_modify["tile"] == "house1":
            s1 = str(level_tile_to_modify["house"].house.collapseCounter * 10)+"%"
            s = s1.encode("utf-8").decode("utf-8")

            pg.init()

            #pg.display.set_caption("INSA_lubrityIII")

            # pg.transform.scale(self.background, (self.window.get_size()))

            pg.draw.rect(self.window, (100, 100, 100), (self.window.get_size()[0] / 2 - 155, 125, 310, 100))


            loop = 1
            while(loop):
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            return
                    if event.type== pg.MOUSEBUTTONDOWN:
                        click = pg.mouse.get_pressed()
                        if click[2]:
                            return
                font = pg.font.Font("assets/font/Forum-Regular.ttf", 25)
                text = font.render(s, 1, (0, 0, 0))
                rect2 =pg.Rect(self.window.get_size()[0]/2-150, 150, 300, 50)
                pg.draw.rect(self.window, (149, 148, 116), rect2, 0, 2, 2)
                self.window.blit(text, (rect2.x + (rect2.width / 2 - text.get_width() / 2),
                                   rect2.y + (rect2.height / 2 - text.get_height() / 2)))
                pg.display.update()