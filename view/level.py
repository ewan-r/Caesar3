import pygame as pg

from controller.level_controller import LevelController
from view.hud import HUD

class Level:
    def __init__(self, entities, grid_length_x, grid_length_y, width, height):
        self.entities = entities
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.grass_tiles = pg.Surface(
            (grid_length_x * 30 * 2, grid_length_y * 30 + 2 * 30)).convert_alpha()

        self.level_controller = LevelController(self)

        # HUD
        self.hud = HUD(self)

        # load functions
        self.tiles = self.level_controller.load_images()
        self.level = self.level_controller.create_level()

        self.temp_tile = None
        self.examine_title = None

    def draw(self, screen, camera):
        screen.blit(self.grass_tiles, (camera.scroll.x, camera.scroll.y))

        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                render_pos =  self.level[x][y]["render_pos"]
                # draw world tiles
                tile = self.level[x][y]["tile"]
                type_tile = self.level[x][y]["type_tile"]
                if tile != "":
                    screen.blit(self.tiles[type_tile][tile],
                                    (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                                     render_pos[1] - (self.tiles[type_tile][tile].get_height() - 30) + camera.scroll.y))

        if self.temp_tile is not None:
            iso_poly = self.temp_tile["iso_poly"]
            iso_poly = [(x + self.grass_tiles.get_width()/2 + camera.scroll.x, y + camera.scroll.y) for x, y in iso_poly]
            if self.temp_tile["collision"]:
                pg.draw.polygon(screen, (255, 0, 0), iso_poly, 3)
            else:
                pg.draw.polygon(screen, (255, 255, 255), iso_poly, 3)
            render_pos = self.temp_tile["render_pos"]
            screen.blit(
                self.temp_tile["image"],
                (
                    render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                    render_pos[1] - (self.temp_tile["image"].get_height() - 30) + camera.scroll.y
                )
            )