import pygame as pg

class Level:

    def __init__(self, entities,grid_length_x, grid_length_y, width, height):
        self.entities = entities
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.grass_tiles = pg.Surface(
            (grid_length_x * 30 * 2, grid_length_y * 30 + 2 * 30)).convert_alpha()
        self.tiles = self.load_images()
        self.level = self.create_level()

        self.temp_tile = None
        self.examine_title = None


    def draw(self, screen, camera):

        screen.blit(self.grass_tiles, (camera.scroll.x, camera.scroll.y))

        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                render_pos =  self.level[x][y]["render_pos"]
                #draw world tiles
                tile = self.level[x][y]["tile"]
                if tile != "":
                    screen.blit(self.tiles[tile],
                                    (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                                     render_pos[1] - (self.tiles[tile].get_height() - 30) + camera.scroll.y))


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


    def create_level(self):

        level = []

        for grid_x in range(self.grid_length_x):
            level.append([])
            for grid_y in range(self.grid_length_y):
                level_tile = self.grid_to_level(grid_x, grid_y)
                level[grid_x].append(level_tile)

                render_pos = level_tile["render_pos"]
                if grid_x == 21:
                    self.grass_tiles.blit(self.tiles["landsRoad"]["landRoad1"],
                                          (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))
                elif (10<=grid_y <17 and grid_x == 0) or (11<=grid_y <21 and grid_x == 1)or (16<=grid_y <21 and grid_x == 2)or (20<=grid_y <40 and 3<=grid_x<7):
                    self.grass_tiles.blit(self.tiles["landsWater"]["landWater1"],
                                          (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))
                elif (10<=grid_y<=30 and 7<=grid_x<=17):
                    self.grass_tiles.blit(self.tiles["lands"]["land2"],
                                          (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))
                    self.grass_tiles.blit(self.tiles["landsForests"]["landForest1"],
                                          (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))
                elif (10 <= grid_y <= 30 and 27 <= grid_x <= 37):
                    self.grass_tiles.blit(self.tiles["lands"]["land2"],
                                          (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))
                    self.grass_tiles.blit(self.tiles["landsMountain"]["landMountain1"],
                                          (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))
                else:
                    self.grass_tiles.blit(self.tiles["lands"]["land1"], (render_pos[0] + self.grass_tiles.get_width()/2, render_pos[1]))


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

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny],
            "tile": tile
            #"collision": False if tile == "" else True
        }

        return out


    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def mouse_to_grid(self, x, y, scroll):
        # transform to world position (removing camera scroll and offset)
        world_x = x - scroll.x - self.grass_tiles.get_width()/2
        world_y = y - scroll.y
        # transform to cart (inverse of cart_to_iso)
        cart_y = (2*world_y - world_x)/2
        cart_x = cart_y + world_x
        # transform to grid coordinates
        grid_x = int(cart_x // 30)
        grid_y = int(cart_y // 30)
        return grid_x, grid_y

    def load_images(self):

        land1 = pg.image.load("C3/Land1a_00081.png").convert_alpha()
        land2 = pg.image.load("C3/Land1a_00094.png").convert_alpha()
        lands = {
            "land1":land1,
            "land2": land2
        }

        landForest1 = pg.image.load("C3/Land1a_00045.png").convert_alpha()
        landsForests = {
            "landForest1":landForest1
        }

        landWater1 = pg.image.load("C3/Land1a_00122.png").convert_alpha()
        landsWater = {
            "landWater1":landWater1
        }

        landCoast1 = pg.image.load("C3/Land1a_00132.png").convert_alpha()
        landsCoast = {
            "landCoast1":landCoast1
        }

        landMountain1 = pg.image.load("C3/Land1a_00295.png").convert_alpha()
        landsMountain = {
            "landMountain1":landMountain1
        }

        landRoad1 = pg.image.load("C3/Land2a_00095.png").convert_alpha()
        landsRoad = {
            "landRoad1":landRoad1
        }


        images = {
            "lands": lands,
            "landsForests":landsForests,
            "landsWater":landsWater,
            "landsCoast":landsCoast,
            "landsMountain":landsMountain,
            "landsRoad":landsRoad
        }

        return images