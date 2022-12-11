from random import choice
import pygame as pg
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

class WalkerController:
    def __init__(self,hud):
        self.l_walkers = []
        self.sprite = pg.image.load("assets/sprites/walker/Carts_00625.png").convert_alpha()
        self.time = 0
        self.hud = hud


    def new_walker(self,  coords, building_controller=0, status=0, spawn_x=0, spawn_y=0, sprite = 0, destination_controller = 0, departure = 0):
        """
        Coords : [x,y] (grid)
        """
        if spawn_x == 0 :      
            spawn_x, spawn_y = self.get_border()
        if sprite == 0:
            sprite = self.sprite
        walker = [sprite, 0 ,0 , spawn_x, spawn_y, coords[0], coords[1], building_controller, status, destination_controller, departure]
        walker[1], walker[2] = self.hud.level.level[walker[3]][walker[4]]["render_pos"]
        self.l_walkers.append(walker)




    def get_border(self):
        l_roads=self.hud.level.level_controller.get_list_pos_sprites("landsRoad")
        l_border_roads = []
        for elem in l_roads:
            if elem[0]==0 or elem[0] == 39 or elem[1]==0 or elem[1]==39:
                l_border_roads.append(elem)
                
        border = choice(l_border_roads)
        return border[0], border[1]


    def random_walk(self, walker):
        possible_path=self.hud.level.level_controller.get_path((walker[3], walker[4]))
        path = choice(possible_path)
        #walker[1],walker[2] = path["render_pos"]
        walker[5],walker[6] = path["grid"]
        self.time = 0

    
    def give_destination(self,walker, coords):
        """
        Coords : [x,y] (grid)
        """
        walker[5], walker[6] = coords[0], coords[1]

    def is_arrived(self,walker):
        if (walker[3] == walker[5] and walker[4] == walker[6]):
            return True
        return False



    def path_finding(self,walker):
        matrix = self.hud.level.level_controller.get_tile_matrix("landsRoad")
        if walker[8] == 0:
            m2 = self.hud.level.level_controller.get_tile_matrix("")
            matrix += m2


        grid = Grid(matrix = matrix)
        if matrix[walker[4]][walker[3]] != 0 and matrix[walker[6]][walker[5]] != 0:
            target_x = walker[5]
            target_y = walker[6]
            start_x = walker[3]
            start_y = walker[4]
            
            start = grid.node(start_x,start_y)
            end = grid.node(target_x,target_y)
            finder = AStarFinder(diagonal_movement= DiagonalMovement.always)
            path,runs = finder.find_path(start,end,grid)
            return path

    def detect_and_repare_buildings (self, walker):
        walker[7].detect_and_repare_buldings(walker)


    def update(self):
        if self.time == 50:
            for walker in self.l_walkers:
                path = self.path_finding(walker)
                
                if path and len(path) >  1:               
                    (walker[3], walker[4]) = path[1]
                    walker[1], walker[2] = self.hud.level.level[walker[3]][walker[4]]["render_pos"]
                    self.time = 0
                if walker[7] != 0 and walker[8]==0:
                    if (self.is_arrived(walker)):
                        walker[7].upgrade()
                        walker[8] = 1
                        self.l_walkers.remove(walker)

                if walker[7] != 0 and walker[8] == 2:
                    if (self.is_arrived(walker)):
                        self.random_walk(walker)
                    self.detect_and_repare_buildings(walker)
                if walker[7] != 0 and walker[8] == 3:
                    if (self.is_arrived(walker)):
                        walker[9].receipt_wheat(walker[10], [walker[5], walker[6]], walker[7])
                        self.l_walkers.remove(walker)
                if walker[7] != 0 and walker[8] == 4:
                    if (self.is_arrived(walker)):
                        walker[7].reset_deliver()
                        self.l_walkers.remove(walker)
                    

        else:
            self.time += 1