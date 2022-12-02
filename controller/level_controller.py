import pygame as pg
import random
class LevelController:
    def __init__(self, level):
        self.level = level
        self.biomes = self.generate_biomes()
        self.buildings = []
        self.economy_buildings = []
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
                    world[x][y]["type_tile"] = "landsForests"
                    if probaTree < 5 : 
                        world[x][y]["tile"] = "landForest45"
                    elif probaTree > 5 and probaTree < 10:
                        world[x][y]["tile"] = "landForest13"
                    elif probaTree <15 and probaTree > 10:
                        world[x][y]["tile"] = "landForest14"
                    elif probaTree < 20 and probaTree > 15:
                        world[x][y]["tile"] = "landForest15"
                    elif probaTree < 25 and probaTree > 20:
                        world[x][y]["tile"] = "landForest16"
                    elif probaTree < 30 and probaTree > 25:
                        world[x][y]["tile"] = "landForest58"
                    elif probaTree < 35 and probaTree > 30:
                        world[x][y]["tile"] = "landForest59"
                    elif probaTree < 40 and probaTree > 35:
                        world[x][y]["tile"] = "landForest60"
                    else:
                        world[x][y]["tile"] = "landForest17"
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
        house1 = pg.image.load("assets/sprites/buildings/Housng1a_00002.png").convert_alpha()
        engineerPost = pg.image.load("assets/sprites/buildings/transport_00056.png").convert_alpha()
        ruin = pg.image.load("assets/sprites/buildings/Land2a_00114.png").convert_alpha()
        farm12 = pg.image.load("assets/sprites/buildings/farm/Commerce_00012.png").convert_alpha()
        farm13 = pg.image.load("assets/sprites/buildings/farm/Commerce_00013.png").convert_alpha()
        farm14 = pg.image.load("assets/sprites/buildings/farm/Commerce_00014.png").convert_alpha()
        farm15 = pg.image.load("assets/sprites/buildings/farm/Commerce_00015.png").convert_alpha()
        farm16 = pg.image.load("assets/sprites/buildings/farm/Commerce_00016.png").convert_alpha()
        farm17 = pg.image.load("assets/sprites/buildings/farm/Commerce_00017.png").convert_alpha()
        granary141 = pg.image.load("assets/sprites/buildings/granary/Commerce_00141.png").convert_alpha()
        granary142 = pg.image.load("assets/sprites/buildings/granary/Commerce_00142.png").convert_alpha()
        granary143 = pg.image.load("assets/sprites/buildings/granary/Commerce_00143.png").convert_alpha()
        granary144 = pg.image.load("assets/sprites/buildings/granary/Commerce_00144.png").convert_alpha()
        granary145 = pg.image.load("assets/sprites/buildings/granary/Commerce_00145.png").convert_alpha()
        granary146 = pg.image.load("assets/sprites/buildings/granary/Commerce_00146.png").convert_alpha()
        granary147 = pg.image.load("assets/sprites/buildings/granary/Commerce_00147.png").convert_alpha()
        granary148 = pg.image.load("assets/sprites/buildings/granary/Commerce_00148.png").convert_alpha()
        granary149 = pg.image.load("assets/sprites/buildings/granary/Commerce_00149.png").convert_alpha()
        granary150 = pg.image.load("assets/sprites/buildings/granary/Commerce_00150.png").convert_alpha()
        granary151 = pg.image.load("assets/sprites/buildings/granary/Commerce_00151.png").convert_alpha()
        granary152 = pg.image.load("assets/sprites/buildings/granary/Commerce_00152.png").convert_alpha()
        reservoir34 = pg.image.load("assets/sprites/buildings/water_buildings/Utilitya_00034.png").convert_alpha()
        reservoir35 = pg.image.load("assets/sprites/buildings/water_buildings/Utilitya_00035.png").convert_alpha()
        reservoir36 = pg.image.load("assets/sprites/buildings/water_buildings/Utilitya_00036.png").convert_alpha()
        reservoir37 = pg.image.load("assets/sprites/buildings/water_buildings/Utilitya_00037.png").convert_alpha()
        reservoir38 = pg.image.load("assets/sprites/buildings/water_buildings/Utilitya_00038.png").convert_alpha()
        reservoir39 = pg.image.load("assets/sprites/buildings/water_buildings/Utilitya_00039.png").convert_alpha()
        reservoir40 = pg.image.load("assets/sprites/buildings/water_buildings/Utilitya_00040.png").convert_alpha()
        reservoir41 = pg.image.load("assets/sprites/buildings/water_buildings/Utilitya_00041.png").convert_alpha()
        reservoir42 = pg.image.load("assets/sprites/buildings/water_buildings/Utilitya_00042.png").convert_alpha()
        aqueducleftandrightfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00121.png").convert_alpha()
        aqueducupanddownfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00122.png").convert_alpha()
        aqueduccorneruprightfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00123.png").convert_alpha()
        aqueduccornerupleftfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00124.png").convert_alpha()
        aqueduccornerbottomrightfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00125.png").convert_alpha()
        aqueduccornerbottomleftfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00126.png").convert_alpha()
        aqueducaboveroadleftrightfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00127.png").convert_alpha()
        aqueducaboveroadupdownfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00128.png").convert_alpha()
        aqueductridownrightfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00129.png").convert_alpha()
        aqueductridownleftfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00130.png").convert_alpha()
        aqueductriupleftfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00131.png").convert_alpha()
        aqueductriuprightfull = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00132.png").convert_alpha()
        
        aqueducleftandright = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00136.png").convert_alpha()
        aqueducupanddown = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00137.png").convert_alpha()
        aqueduccornerupright = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00138.png").convert_alpha()
        aqueduccornerupleft = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00139.png").convert_alpha()
        aqueduccornerbottomright = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00140.png").convert_alpha()
        aqueduccornerbottomleft = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00141.png").convert_alpha()
        aqueducaboveroadleftright = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00142.png").convert_alpha()
        aqueducaboveroadupdown = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00143.png").convert_alpha()
        aqueductridownright = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00144.png").convert_alpha()
        aqueductridownleft = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00145.png").convert_alpha()
        aqueductriupleft = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00146.png").convert_alpha()
        aqueductriupright = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00147.png").convert_alpha()
        aqueducleftrightupdown = pg.image.load("assets/sprites/buildings/aqueducs/Land2a_00148.png").convert_alpha()
        buildings = {
            "house1": house1,
            "engineerPost": engineerPost,
            "ruin": ruin,
            "farm12" : farm12,
            "farm13" : farm13,
            "farm14" : farm14,
            "farm15" : farm15,
            "farm16" : farm16,
            "farm17" : farm17,
            "granary141" : granary141,
            "granary142" : granary142,
            "granary143" : granary143,
            "granary144" : granary144,
            "granary145" : granary145,
            "granary146" : granary146,
            "granary147" : granary147,
            "granary148" : granary148,
            "granary149" : granary149,
            "granary150" : granary150,
            "granary151" : granary151,
            "granary152" : granary152,
            "reservoir34" : reservoir34,
            "reservoir35" : reservoir35,
            "reservoir36" : reservoir36,
            "reservoir37" : reservoir37,
            "reservoir38" : reservoir38,
            "reservoir39" : reservoir39,
            "reservoir40" : reservoir40,
            "reservoir41" : reservoir41,
            "reservoir42" : reservoir42,
            "aqueducleftandrightfull" : aqueducleftandrightfull,
            "aqueducupanddownfull" : aqueducupanddownfull,
            "aqueduccorneruprightfull" : aqueduccorneruprightfull,
            "aqueduccornerupleftfull" : aqueduccornerupleftfull,
            "aqueduccornerbottomrightfull" : aqueduccornerbottomrightfull,
            "aqueduccornerbottomleftfull" : aqueduccornerbottomleftfull,
            "aqueducaboveroadleftrightfull" : aqueducaboveroadleftrightfull,
            "aqueducaboveroadupdownfull" : aqueducaboveroadupdownfull,
            "aqueductridownrightfull" : aqueductridownrightfull,
            "aqueductridownleftfull" : aqueductridownleftfull,
            "aqueductriupleftfull" : aqueductriupleftfull,
            "aqueductriuprightfull" : aqueductriuprightfull,
            "aqueducright" : aqueducleftandright,
            "aqueducup" : aqueducupanddown,
            "aqueducleft" : aqueducleftandright,
            "aqueducdown" : aqueducupanddown,
            "aqueducleftright" : aqueducleftandright,
            "aqueducupdown" : aqueducupanddown,
            "aqueducrightdown" : aqueduccornerupright,
            "aqueducleftdown" : aqueduccornerupleft,
            "aqueducleftup" : aqueduccornerbottomright,
            "aqueducrightup" : aqueduccornerbottomleft,
            "aqueducaboveroadleftright" : aqueducaboveroadleftright,
            "aqueducaboveroadupdown" : aqueducaboveroadupdown,
            "aqueducleftrightdown" : aqueductridownright,
            "aqueducleftupdown" : aqueductridownleft,
            "aqueducleftrightup" : aqueductriupleft,
            "aqueducrightupdown" : aqueductriupright,
            "aqueducleftrightupdown" : aqueducleftrightupdown,
        }
        land81 = pg.image.load("assets/sprites/lands/Land1a_00081.png").convert_alpha()
        land94 = pg.image.load("assets/sprites/lands/Land1a_00094.png").convert_alpha()
        landFarm1 = pg.image.load("assets/sprites/lands/Land1a_00025.png").convert_alpha()
        lands = {
            "land81": land81,
            "land94": land94,
            "landFarm1": landFarm1
        }
        landForest45 = pg.image.load("assets/sprites/lands/Land1a_00045.png").convert_alpha()
        landForest13 = pg.image.load("assets/sprites/lands/Land1a_00013.png").convert_alpha()
        landForest14 = pg.image.load("assets/sprites/lands/Land1a_00014.png").convert_alpha()
        landForest15 = pg.image.load("assets/sprites/lands/Land1a_00015.png").convert_alpha()
        landForest16 = pg.image.load("assets/sprites/lands/Land1a_00016.png").convert_alpha()
        landForest17 = pg.image.load("assets/sprites/lands/Land1a_00017.png").convert_alpha()
        landForest58 = pg.image.load("assets/sprites/lands/Land1a_00058.png").convert_alpha()
        landForest59 = pg.image.load("assets/sprites/lands/Land1a_00059.png").convert_alpha()
        landForest60 = pg.image.load("assets/sprites/lands/Land1a_00060.png").convert_alpha()
        landsForests = {
            "landForest45": landForest45,
            "landForest13" : landForest13,
            "landForest14" : landForest14,
            "landForest15" : landForest15,
            "landForest16" : landForest16,
            "landForest17" : landForest17,
            "landForest58" : landForest58,
            "landForest59" : landForest59,
            "landForest60" : landForest60,
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
            "buildings": buildings
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

    def get_neighbors_tile(self, coords):
        neighbors = []


        if coords[0] < self.level.grid_length_x and coords[1] < self.level.grid_length_y:
            if coords[0] >= 0 and coords[1] >= 0:
                if coords[0] != self.level.grid_length_x-1:
                    down = self.level.level[coords[0]-1][coords[1]]
                    print(down["tile"])
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

    def get_fictive_neighbors(self, list_of_previewed,index):
        neighbors = []
        if len(list_of_previewed) >= 1:
            if index == len(list_of_previewed):
            
                previous_tile_previewed = list_of_previewed[index-1]
                neighbors.append(previous_tile_previewed)
            if (len(list_of_previewed) >= 3) and index != len(list_of_previewed):

                previous_tile_previewed = list_of_previewed[index - 1]
                next_tile_previewed = list_of_previewed[len(list_of_previewed)-1]
                neighbors.append(previous_tile_previewed)
                neighbors.append(next_tile_previewed)
        
        return neighbors

    def get_position_fictive_neighbor (self, coords, neighbor):
        if (coords[0] == neighbor["grid"][0]-1 and coords[1] == neighbor["grid"][1]):
            return "down"
        if (coords[0] == neighbor["grid"][0]+1 and coords[1] == neighbor["grid"][1]):
            return "up"
        if (coords[1] == neighbor["grid"][1]+1 and coords[0] == neighbor["grid"][0]): 
            return "right"
        if (coords[1] == neighbor["grid"][1]-1 and coords[0] == neighbor["grid"][0]):
            return "left"
        return "empty"

    def get_real_neighbors (self, tile_to_get_neighors_from,type_tile_world, level):
        """
        Return a list with the list of neighbors which the tile field contains tile_world

        Args:
            tile_to_get_neighors_from (list): tile which we need to get neighbors from
            type_tile(str): type of neighbors
            level (list) : list of all tiles of the world
        """
        print(tile_to_get_neighors_from)
        x = tile_to_get_neighors_from["grid"][0]
        y = tile_to_get_neighors_from["grid"][1]
        print(level[x][y])
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
        
