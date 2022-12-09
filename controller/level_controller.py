import pygame as pg
import numpy as np

class LevelController:
    """A LevelController."""
    def __init__(self, level):
        """LevelController constructor.
        
        Argument:
            level -- level to control
        """
        self.level = level

    def create_level(self):
        """Create a level.
        
        Returns:
            a level created
        """
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
        """Create properties of a tile.
        
        Arguments:
            grid_x -- grid abscissa coordinate
            grid_y -- grid ordinate coordinate

        Returns:
            properties of a tile
        """
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
            tile = "roadRight"
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
        """Convert cartesian coordinates to isometric coordinates.
        
        Returns:
            isometric coordinates
        """
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def mouse_to_grid(self, x, y, scroll):
        """Convert mouse coordinates to be compatible with the grid level.
        
        Returns:
            grid coordinates
        """
        # transform to world position (removing camera scroll and offset)
        world_x = x - scroll.x - self.level.grass_tiles.get_width()/2
        world_y = y - scroll.y
        # transform to cart (inverse of cart_to_iso)
        cart_y = (2*world_y - world_x)/2
        cart_x = cart_y + world_x
        # transform to grid coordinates
        grid_x = int(cart_x // 30)
        grid_y = int(cart_y // 30)
        
        return grid_x, grid_y

    def load_images(self):
        """Load images for sprites.
        
        Returns:
            each image corresponding to mul category
        """
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

        roadupanddown = pg.image.load("assets/sprites/lands/Land2a_00096.png").convert_alpha()

        roadDown = pg.image.load("assets/sprites/lands/Land2a_00096.png").convert_alpha()
        roadLeft = pg.image.load("assets/sprites/lands/Land2a_00093.png").convert_alpha()
        roadRight = pg.image.load("assets/sprites/lands/Land2a_00093.png").convert_alpha()

        roadIntersectionCenter = pg.image.load("assets/sprites/lands/Land2a_00110.png").convert_alpha()
        roadIntersectionUp = pg.image.load("assets/sprites/lands/Land2a_00108.png").convert_alpha()
        roadIntersectionDown = pg.image.load("assets/sprites/lands/Land2a_00106.png").convert_alpha()
        roadIntersectionLeft = pg.image.load("assets/sprites/lands/Land2a_00107.png").convert_alpha()
        roadIntersectionRight = pg.image.load("assets/sprites/lands/Land2a_00109.png").convert_alpha()

        roadRightNextToUp  = pg.image.load("assets/sprites/lands/Land2a_00097.png").convert_alpha()
        roadRightNextToDown  = pg.image.load("assets/sprites/lands/Land2a_00100.png").convert_alpha()
        roadDownNextToLeft = pg.image.load("assets/sprites/lands/Land2a_00097.png").convert_alpha()
        roadDownNextToRight = pg.image.load("assets/sprites/lands/Land2a_00098.png").convert_alpha()
        roadLeftNextToUp = pg.image.load("assets/sprites/lands/Land2a_00098.png").convert_alpha()
        roadLeftNextToDown = pg.image.load("assets/sprites/lands/Land2a_00099.png").convert_alpha()
        roadUpNextToLeft = pg.image.load("assets/sprites/lands/Land2a_00100.png").convert_alpha()
        roadUpNextToRight = pg.image.load("assets/sprites/lands/Land2a_00099.png").convert_alpha()

        landsRoad = {
            "roadup": roadupanddown,
            "roadown": roadupanddown,

            "roadLeft": roadLeft,
            "roadRight": roadRight,

            "roadIntersectionCenter": roadIntersectionCenter,
            "roadIntersectionUp": roadIntersectionUp,
            "roadIntersectionDown": roadIntersectionDown,
            "roadIntersectionRight": roadIntersectionRight,
            "roadIntersectionLeft": roadIntersectionLeft,

            "roadRightNextToUp": roadRightNextToUp,
            "roadRightNextToDown": roadRightNextToDown,
            "roadDownNextToLeft": roadDownNextToLeft,
            "roadDownNextToRight": roadDownNextToRight,
            "roadLeftNextToUp": roadLeftNextToUp,
            "roadLeftNextToDown": roadLeftNextToDown,
            "roadUpNextToLeft": roadUpNextToLeft,
            "roadUpNextToRight": roadUpNextToRight
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
        """Get the positions of sprites that correspond to a category.
        
        Argument:
            type_tile -- type of the tile where is the sprite

        Returns:
            a list containing the positions of sprites that correspond to a category
        """
        list_pos_sprites = []

        for grid_x in range(self.level.grid_length_x):
            for grid_y in range(self.level.grid_length_y):
                level_tile = self.level.level[grid_x][grid_y]

                if level_tile['type_tile'] == type_tile:
                    list_pos_sprites.append(level_tile['grid'])
        
        return list_pos_sprites

    def get_real_neighbors(self, tile_to_get_neighors_from, type_tile_world, level):
        """
        Return a list with the list of neighbors which the tile field contains tile_world
        Args:
            tile_to_get_neighors_from (list): tile which we need to get neighbors from
            type_tile_world(str): type of neighbors
            level (list) : list of all tiles of the world
        """
        x = tile_to_get_neighors_from["grid"][0]
        y = tile_to_get_neighors_from["grid"][1]
        neighbors = []

        if ( type_tile_world in level[x-1][y]["tile"]):
            neighbors.append(level[x-1][y])
        if (type_tile_world in level[x+1][y]["tile"]):
            neighbors.append(level[x+1][y])
        if (type_tile_world in level[x][y-1]["tile"]):
            neighbors.append(level[x][y-1])
        if (type_tile_world in level[x][y+1]["tile"]):
            neighbors.append(level[x][y+1])
        return neighbors

    def get_tile_matrix(self, type_tile):
        """        
        Argument:
            type_tile -- type of the tile where is the sprite
        Returns:
            a matrix of 1 (tile of type_tile found) and 0
         """
        tile_matrix = np.zeros((40,40))

        for grid_x in range(self.level.grid_length_x):
            for grid_y in range(self.level.grid_length_y):
                level_tile = self.level.level[grid_x][grid_y]

                if level_tile['type_tile'] == type_tile:
                    tile_matrix[grid_y][grid_x] = 1
         
        return tile_matrix


    def get_neighbors_tile(self, coords):
        neighbors = []

        if coords[0] < self.level.grid_length_x and coords[1] < self.level.grid_length_y:
            if coords[0] >= 0 and coords[1] >= 0:
                if coords[0] != self.level.grid_length_x-1:
                    down = self.level.level[coords[0]-1][coords[1]]
                    if ("aqueduc" in down["tile"]):
                        neighbors.append("down")
                if coords[1] != self.level.grid_length_y-1:
                    left = self.level.level[coords[0]][coords[1]+1]
                    if "aqueduc" in left["tile"]:
                        neighbors.append("left")
                if coords[0] != self.level.grid_length_x+1:
                    up = self.level.level[coords[0]+1][coords[1]]
                    if "aqueduc" in up["tile"]: 
                        neighbors.append("up")
                if coords[1] != self.level.grid_length_y+1:
                    right = self.level.level[coords[0]][coords[1]-1]
                    if "aqueduc" in right   ["tile"]:
                        neighbors.append("right")
                
        return neighbors
    
    def find_right_tile(self,tile_to_change, neighbors):
        #print("Tile to change :")
        #print(" ")
        #print(tile_to_change)
        if (len(neighbors) >= 1):
            up = ""
            down =""
            right = ""
            left = ""
            isUp = False
            isDown = False
            isRight = False
            isLeft = False
            if ("up" in neighbors):
                up = "up"
                isUp = True
            if ("down" in neighbors):
                down = "down"
                isDown = True
            if ("right" in neighbors):
                right = "right"
                isRight = True
            if ("left" in neighbors):
                left = "left"
                isLeft = False
            if (isUp or isDown or isRight or isLeft):
                tile_to_change["tile"] = "aqueduc"+left+right+up+down
                tile_to_change["type_tile"] = "buildings"