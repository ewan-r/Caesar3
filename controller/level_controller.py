import pygame as pg
import controller.utils

class LevelController:
    def __init__(self, level):
        self.level = level

    def create_level(self):
        level = []

        for grid_x in range(self.level.grid_length_x):
            level.append([])
            for grid_y in range(self.level.grid_length_y):
                level_tile = self.grid_to_level(grid_x, grid_y)
                level[grid_x].append(level_tile)

                render_pos = level_tile["render_pos"]
                
                self.level.grass_tiles.blit(self.level.tiles["lands"]["land81"], (render_pos[0] + self.level.grass_tiles.get_width()/2, render_pos[1]))

        return level

    def grid_to_level(self, grid_x, grid_y):
        rect = [
            (grid_x * 30, grid_y * 30),
            (grid_x * 30 + 30, grid_y * 30),
            (grid_x * 30 + 30, grid_y * 30 + 30),
            (grid_x * 30, grid_y * 30 + 30)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        tile=""
        type_tile = ""

        if grid_x == 21:
            type_tile = "landsRoad"
            tile = "landRoad1"
        elif (10 <= grid_y < 17 and grid_x == 0) or (11 <= grid_y < 21 and grid_x == 1) or (
                16 <= grid_y < 21 and grid_x == 2) or (20 <= grid_y < 40 and 3 <= grid_x < 7):
            type_tile = "landsWater"
            tile = "landWater1"
        elif (10 <= grid_y <= 30 and 7 <= grid_x <= 17):
            type_tile = "landsForests"
            tile="landForest45"
        elif (10 <= grid_y <= 30 and 27 <= grid_x <= 37):
            type_tile = "landsMountain"
            tile="landMountain1"

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny],
            "type_tile": type_tile,
            "tile": tile
            #"collision": False if tile == "" else True
        }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    # how to use scroll when the function is called ???
    def mouse_to_grid(self, x, y):
        # transform to world position (removing camera scroll and offset)
        world_x = x - self.level.grass_tiles.get_width()/2
        world_y = y
        # transform to cart (inverse of cart_to_iso)
        cart_y = (2*world_y - world_x)/2
        cart_x = cart_y + world_x
        # transform to grid coordinates
        grid_x = int(cart_x // 30)
        grid_y = int(cart_y // 30)
        
        return grid_x, grid_y

    def load_images(self):
        land81 = pg.image.load("assets/sprites/lands/Land1a_00081.png").convert_alpha()
        land94 = pg.image.load("assets/sprites/lands/Land1a_00094.png").convert_alpha()
        lands = {
            "land81": land81,
            "land94": land94
        }

        landForest45 = pg.image.load("assets/sprites/lands/Land1a_00045.png").convert_alpha()
        landsForests = {
            "landForest45": landForest45
        }

        landWater1 = pg.image.load("assets/sprites/lands/Land1a_00122.png").convert_alpha()
        landsWater = {
            "landWater1": landWater1
        }

        landCoast1 = pg.image.load("assets/sprites/lands/Land1a_00132.png").convert_alpha()
        landsCoast = {
            "landCoast1": landCoast1
        }

        landMountain1 = pg.image.load("assets/sprites/lands/Land1a_00295.png").convert_alpha()
        landsMountain = {
            "landMountain1": landMountain1
        }

        landRoad1 = pg.image.load("assets/sprites/lands/Land2a_00095.png").convert_alpha()
        landsRoad = {
            "landRoad1": landRoad1
        }

        images = {
            "lands": lands,
            "landsForests": landsForests,
            "landsWater": landsWater,
            "landsCoast": landsCoast,
            "landsMountain": landsMountain,
            "landsRoad": landsRoad
        }

        return images

    def get_list_pos_sprites(self, type_tile):
        """"""
        pos_sprites = []

        for grid_x in range(self.level.grid_length_x):
            for grid_y in range(self.level.grid_length_y):
                level_tile = self.grid_to_level(grid_x, grid_y)

                if level_tile['type_tile'] == type_tile:
                    pos_sprites.append(level_tile['grid'])
        
        return pos_sprites

    def mouse_next_to_sprite(self, current_mouse_pos_grid, list_pos_sprites):
        """"""

        is_next_to_sprite = False

        list_pos_sprites_without_brackets = controller.utils.convert_list_coords_brackets_parenthesis(list_pos_sprites)

        if current_mouse_pos_grid not in list_pos_sprites_without_brackets:
            coord_x, coord_y = current_mouse_pos_grid

            if (coord_x, coord_y-1) in list_pos_sprites_without_brackets or (coord_x, coord_y+1) in list_pos_sprites_without_brackets or (coord_x-1, coord_y) in list_pos_sprites_without_brackets or (coord_x+1, coord_y) in list_pos_sprites_without_brackets:
                is_next_to_sprite = True

        return is_next_to_sprite