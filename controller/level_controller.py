import pygame as pg
import random
class LevelController:
    def __init__(self, level):
        self.level = level
        self.biomes = self.generate_biomes()

    def create_level(self):
        level = []

        for grid_x in range(self.level.grid_length_x):
            level.append([])
            for grid_y in range(self.level.grid_length_y):
                level_tile = self.grid_to_level(grid_x, grid_y)
                level[grid_x].append(level_tile)

                render_pos = level_tile["render_pos"]
                
                self.level.grass_tiles.blit(self.level.tiles["lands"]["land81"], (render_pos[0] + self.level.grass_tiles.get_width()/2, render_pos[1]))
        
        
        for forest in self.biomes['forests']:
            self.generate_forest(level, forest)
        for farm in self.biomes['farms']:
            self.generate_cultivable_lands(level,farm)
        for ocean in self.biomes['oceans']:
            self.generate_seas(level, ocean)
        
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
            tile = "roadRight"
        """
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
        """
        
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
    def generate_biomes(self):
            
            forests = []
            oceans = []
            farms = []

            numberForest = random.randint(4,6)
            numberOcean = random.randint(2,3)
            numberFarms = random.randint(3,5)


            for i in range (1,numberForest,1):
                
                sizeForest = random.randint(10,20)
                coordinatesForest = (random.randint(1,self.level.grid_length_x - sizeForest - 1),random.randint(1,self.level.grid_length_y - sizeForest - 1))
                forest = [coordinatesForest[0],coordinatesForest[1],sizeForest]
                forests.append(forest)
            
            for i in range (1,numberOcean):
                
                sizeOcean = random.randint(4,10)
                coordinatesOcean =  (random.randint(1,self.level.grid_length_x - sizeOcean - 1),random.randint(1,self.level.grid_length_y - sizeOcean - 1))
                ocean = [coordinatesOcean[0], coordinatesOcean[1], sizeOcean]
                oceans.append(ocean)
            for i in range (1,numberFarms):
                
                sizeFarms = random.randint(4,6)
                coordinatesFarms = (random.randint(1,self.level.grid_length_x - sizeFarms - 1),random.randint(1,self.level.grid_length_y - sizeFarms - 1))
                farm = [coordinatesFarms[0], coordinatesFarms[1], sizeFarms]
                farms.append(farm)
            
            out = {
                'forests' : forests,
                'oceans' : oceans,
                'farms' : farms
            }
            return out

    def generate_forest(self, world ,forestParams):

        for x in range (forestParams[0], forestParams[0]+forestParams[2],1):

            for y in range (forestParams[1], forestParams[1]+forestParams[2],1):

                probaTree = random.randint(1,100)

                if probaTree < 45:
                    world[x][y]["tile"] = "landForest45"
                    world[x][y]["type_tile"] = "landsForests"
                else:
                    world[x][y]["tile"] = ""
    
    def generate_seas(self, world, seaParams):        
        yOffset = random.randint(1,4)
        for x in range (seaParams[0], seaParams[0] + seaParams[2]):
            
            for y in range (seaParams[1], seaParams[1] + seaParams[2]):
            
                world[x][y]["tile"] = "landWater1"
                world[x][y]["type_tile"] = "landsWater"

    def generate_cultivable_lands (self, world, cultivableParams):
        for x in range (cultivableParams[0],cultivableParams[0]+cultivableParams[2]):
            for y in range (cultivableParams[1],cultivableParams[1]+cultivableParams[2]):
                world[x][y]["tile"] = "landFarm1"
                world[x][y]["type_tile"] = "lands"

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def mouse_to_grid(self, x, y, scroll):
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
        house1 = pg.image.load("assets/sprites/lands/Housng1a_00002.png").convert_alpha()
        houses = {
            "house1": house1
        }
        land81 = pg.image.load("assets/sprites/lands/Land1a_00081.png").convert_alpha()
        land94 = pg.image.load("assets/sprites/lands/Land1a_00094.png").convert_alpha()
        landFarm1 = pg.image.load("assets/sprites/lands/Land2a_00037.png").convert_alpha()
        lands = {
            "land81": land81,
            "land94": land94,
            "landFarm1": landFarm1
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

        roadUp = pg.image.load("assets/sprites/lands/Land2a_00096.png").convert_alpha()
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
            "roadUp": roadUp,
            "roadDown": roadDown,
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
            "landsRoad": landsRoad,
            "houses": houses
        }

        return images

    def get_list_pos_sprites(self, type_tile):
        """Get the positions of sprites of a certain type.
        
        Argument:
            type_tile -- type of the tile where is the sprite

        Returns:
            a list containing the positions of sprites of a certain type
        """
        list_pos_sprites = []

        for grid_x in range(self.level.grid_length_x):
            for grid_y in range(self.level.grid_length_y):
                level_tile = self.level.level[grid_x][grid_y]

                if level_tile['type_tile'] == type_tile:
                    list_pos_sprites.append(level_tile['grid'])
        
        return list_pos_sprites

    def get_neighbors(self, coords):
        """"""
        neighbors = []
        valid_neighbor = True

        if coords[0] < self.level.grid_length_x and coords[1] < self.level.grid_length_y:
            if coords[0] >= 0 and coords[1] >= 0:
                if coords[0] == self.level.grid_length_x-1 or coords[1] == self.level.grid_length_y-1:
                    valid_neighbor = False
                
                if valid_neighbor:
                    up = self.level.level[coords[0]+1][coords[1]]
                    down = self.level.level[coords[0]-1][coords[1]]
                    right = self.level.level[coords[0]][coords[1]+1]
                    left = self.level.level[coords[0]][coords[1]-1]

                    # up
                    if up['type_tile'] == "landsRoad": 
                        neighbors.append(up)
                    # down
                    if down['type_tile'] == "landsRoad":
                        neighbors.append(down)
                    # right
                    if right['type_tile'] == "landsRoad":
                        neighbors.append(right)
                    # left
                    if left['type_tile'] == "landsRoad":
                        neighbors.append(left)
        
        return neighbors
        
