from numpy import size
import pygame as pg
from .settings import TILE_SIZEX, TILE_SIZEY
import random


class World:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.biomes = self.generate_biomes()

        self.grass_lands = pg.Surface((width,height))
        self.tiles = self.load_images()
        self.world = self.create_world()
        


    def create_world(self):

        world = []
        
        #Il faut ici appeler la fonction generate_biomes qui retourne un dico qui retourne des dicos de
        #D'infos sur les biomes.
        for grid_x in range(self.grid_length_x):
            world.append([])
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

                render_pos = world_tile["render_pos"]
                self.grass_lands.blit(self.tiles["grass_land"], (render_pos[0] + self.width/2, render_pos[1] + self.height/4))

        for forest in self.biomes['forests']:
            self.generate_forest(world, forest)
        #self.generate_forest(world,[5,5,10],[17,10,15])
        #On met d'abord que des tiles d'herbes puis on met des tiles pour former les biomes
        for ocean in self.biomes['oceans']:
            self.generate_seas(world, ocean)

        return world

    def grid_to_world(self, grid_x, grid_y):

        rect = [
            (grid_x * TILE_SIZEX, grid_y * TILE_SIZEY),
            (grid_x * TILE_SIZEX + TILE_SIZEX, grid_y * TILE_SIZEY),
            (grid_x * TILE_SIZEX + TILE_SIZEX, grid_y * TILE_SIZEY + TILE_SIZEY),
            (grid_x * TILE_SIZEX, grid_y * TILE_SIZEY + TILE_SIZEY)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        minx = min ([x for x,y in iso_poly])
        miny = min ([y for x,y in iso_poly])

        randInt = random.randint(1,100)
        if randInt < 10:
            tile = "tree"

        else:
            tile = ""
        
        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny],
            "tile": tile
        }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def load_images (self):
        grass_land = pg.image.load("../assets/sprites/lands/Land1a_00081.png").convert_alpha()
        tree = pg.image.load("../assets/sprites/lands/Land1a_00045.png").convert_alpha()
        tree2 = pg.image.load("../assets/sprites/lands/Land1a_00122.png").convert_alpha()
        water = pg.image.load("../assets/sprites/lands/Land1a_00122.png").convert_alpha()
        
        return { "grass_land": grass_land, "tree": tree, "tree2": tree2, "water": water }
    def generate_biomes(self):
        
        forests = []
        oceans = []

        numberForest = random.randint(2,5)
        numberOcean = random.randint(2,3)
        
        for i in range (1,numberForest,1):
            coordinatesForest = (random.randint(1,20),random.randint(1,20))
            sizeForest = random.randint(4,15)
            forest = [coordinatesForest[0],coordinatesForest[1],sizeForest]
            forests.append(forest)
        
        for i in range (1,numberOcean):
            coordinatesOcean =  (random.randint(1,20),random.randint(1,20))
            sizeOcean = random.randint(4,20)
            ocean = [coordinatesOcean[0], coordinatesOcean[1], sizeOcean]
            oceans.append(ocean)
        
        
        out = {
            'forests' : forests,
            'oceans' : oceans
        }
        return out

    def generate_forest(self, world ,forestParams):

        for x in range (forestParams[0], forestParams[0]+forestParams[2],1):

            for y in range (forestParams[1], forestParams[1]+forestParams[2],1):

                probaTree = random.randint(1,100)

                if probaTree < 45:
                    world[x][y]["tile"] = "tree"
                else:
                    world[x][y]["tile"] = ""
    
    def generate_seas(self, world, seaParams):        
        #How to generate seas:
        #Put water tile first and then we identify case around
        yOffset = random.randint(1,4)

        for x in range (seaParams[0], seaParams[0] + seaParams[2]):
            
            for y in range (seaParams[1], seaParams[1] + seaParams[2]):
            
                world[x][y]["tile"] = "water"
        

    def generate_lands(self):
        pass
    def generate_stones(self):
        pass
    def generate_cliffs(self):
        pass
