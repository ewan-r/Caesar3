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
        self.foreground = []
        self.walkers = []
        self.grass_tiles = pg.Surface(
            (grid_length_x * 30 * 2, grid_length_y * 30 + 2 * 30)).convert_alpha()

        self.level_controller = LevelController(self)

        # HUD
        self.hud = HUD(self)
        self.hud.display_hud()

        # load functions
        self.tiles = self.level_controller.load_images()
        self.level = self.level_controller.create_level()
        self.temp_tile = None
        self.examine_title = None
        self.preview_aqueduc = []
    def draw(self, screen, camera):
        screen.blit(self.grass_tiles, (camera.scroll.x, camera.scroll.y))
        coords_world_to_blit = []
        for k in range (self.grid_length_x):
            for y in range (2*k+1):
                if (y < k):
                    x = k
                    coords_world_to_blit.append([x,y])
                elif y > k:
                    x = y - k - 1
                    y = k
                    coords_world_to_blit.append([x,y])
            coords_world_to_blit.append([k,k])
        print(coords_world_to_blit)
        for coord in coords_world_to_blit:
            x = coord[0]
            y = coord[1]
            render_pos =  self.level[x][y]["render_pos"]
            # draw world tiles
            tile = self.level[x][y]["tile"]
            type_tile = self.level[x][y]["type_tile"]
            attached_to_building = self.level[x][y]["attached_to_building"]
            if tile != "" and type_tile != "buildings" and not(attached_to_building):
                screen.blit(self.tiles[type_tile][tile],
                                (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                                render_pos[1] - (self.tiles[type_tile][tile].get_height() - 30) + camera.scroll.y))
            elif type_tile == "buildings":
                if (self.is_water_for_reservoir(tile)):
                    self.foreground.append(self.level[x][y])
                else:
                    #If the building is larger than one tile squared then we need to make sure it is on the grid
                    if self.tiles[type_tile][tile].get_width() >= 60 and self.tiles[type_tile][tile].get_width() <=120:
                        screen.blit(self.tiles[type_tile][tile],
                                        (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x - (self.tiles[type_tile][tile].get_width()/4),
                                        render_pos[1] - (self.tiles[type_tile][tile].get_height() - 30) + camera.scroll.y))
                    elif (self.tiles[type_tile][tile].get_width() >= 121):
                        screen.blit(self.tiles[type_tile][tile],
                                        (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x - 90,
                                        render_pos[1] - (self.tiles[type_tile][tile].get_height() - 45) + camera.scroll.y))
                    else:
                        screen.blit(self.tiles[type_tile][tile],
                                        (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                                        render_pos[1] - (self.tiles[type_tile][tile].get_height() - 30) + camera.scroll.y))
        self.draw_animations_foreground(screen,camera)
        self.draw_preview_aqueduc(screen,camera)
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

    def draw_preview_aqueduc(self,screen,camera):
        #Il faudrait que la liste soit ordonnée dans l'ordre de display
        tiles = self.preview_aqueduc
        #print("Tiles to blit :")
        #print(" ")
        #print(tiles)
        for tile_to_preview in tiles:
            render_pos =  tile_to_preview["render_pos"]
            # draw world tiles
            tile = tile_to_preview["tile"]
            type_tile = tile_to_preview["type_tile"]
            screen.blit(self.tiles[type_tile][tile],
                                            (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                                            render_pos[1] - (self.tiles[type_tile][tile].get_height() - 30) + camera.scroll.y))

    def is_water_for_reservoir(self,tile_to_test):
        x = [str(x) for x in range (35,43)]
        if ("reservoir" in tile_to_test):
            for X in x:
                if (X in tile_to_test):
                    return True
        return False

    def draw_animations_foreground(self,screen,camera):

        for tile_to_blit in self.foreground:
            type_tile = tile_to_blit["type_tile"]
            tile = tile_to_blit["tile"]
            render_pos = tile_to_blit["render_pos"]
            screen.blit(self.tiles[type_tile][tile],
            (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x - 44,
                                            render_pos[1] - (self.tiles[type_tile][tile].get_height() - 40) + camera.scroll.y))