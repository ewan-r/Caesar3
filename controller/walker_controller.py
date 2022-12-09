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


    def new_walker(self, coords, spawn_x=0, spawn_y=0):
        """
        Coords : [x,y] (grid)
        """
        if spawn_x == 0 :      
            spawn_x, spawn_y = self.get_border()
        walker = [self.sprite,0 ,0 , spawn_x, spawn_y, coords[0], coords[1]]
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


    def random_walk(self):
        if self.time == 100 :
            for walker in self.l_walkers:
                possible_path=self.hud.level.level_controller.get_path((walker[3], walker[4]))
                path = choice(possible_path)
                walker[1],walker[2] = path["render_pos"]
                walker[3],walker[4] = path["grid"]
                self.time = 0
        else:
            self.time += 1

    
    def give_destination(walker, coords):
        """
        Coords : [x,y] (grid)
        """
        walker[5], walker[6] = coords[0], coords[1]

    def is_arrived(walker, coords):
        return (walker[3], walker[4] == coords[0], coords[1])


    def path_finding(self,walker):
        matrix = self.hud.level.level_controller.get_tile_matrix("landsRoad")
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


    def update(self):
        if self.time == 50:
            for walker in self.l_walkers:
                path = self.path_finding(walker)
                
                if path and len(path) >  1:               
                        (walker[3], walker[4]) = path[1]
                        walker[1], walker[2] = self.hud.level.level[walker[3]][walker[4]]["render_pos"]
                        self.time = 0
        else:
            self.time += 1








