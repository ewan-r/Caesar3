from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class HUDButtonController():
    """A HUDButtonController."""  

    def __init__(self, hud):
        """HUDButtonController constructor.
        
        Argument:
            hud -- HUD to be updated
        """
        self.hud = hud

    def create_road(self, click_pos, pos_mouse):
        """Create a road.
        
        Argument:
            grid_coords -- grid coordinates of a cell
        """

        matrix = self.hud.level.level_controller.get_tile_matrix("landsRoad")
        grid = Grid(matrix = matrix)

        start_x = click_pos[0]
        start_y = click_pos[1]
        target_x = pos_mouse[0]
        target_y = pos_mouse[1]

        start = grid.node(start_x,start_y)
        end = grid.node(target_x,target_y)

        finder = AStarFinder()
        path = finder.find_path(start, end, grid)
        grid.cleanup()
        

        if path:
            points = []

            for point in path:
                x = point[0][0]
                y = point[0][1]
                points.append((x,y))
                break

            for pt in points:
                tile_to_modify = self.hud.level.level[pt[0]][pt[1]]
                tile_to_modify['type_tile'] = "landsRoad"
                tile_to_modify['tile'] = "roadIntersectionCenter"

        """
        # check limits of the board
        if grid_coords[0] < self.hud.level.grid_length_x and grid_coords[1] < self.hud.level.grid_length_y:
            if grid_coords[0] >= 0 and grid_coords[1] >= 0:
                tile_to_modify = self.hud.level.level[grid_coords[0]][grid_coords[1]]
            
                # grass terrain
                if tile_to_modify['type_tile'] == "":
                    tile_to_modify['type_tile'] = "landsRoad"
                    
                    neighbors = self.hud.level.level_controller.get_neighbors(grid_coords)

                    if tile_to_modify['grid'][0] == self.hud.level.grid_length_x-1 or tile_to_modify['grid'][1] == self.hud.level.grid_length_y-1:
                        tile_to_modify['tile'] = "roadIntersectionCenter"
                    else:
                        up = self.hud.level.level[grid_coords[0]+1][grid_coords[1]]
                        down = self.hud.level.level[grid_coords[0]-1][grid_coords[1]]
                        right = self.hud.level.level[grid_coords[0]][grid_coords[1]+1]
                        left = self.hud.level.level[grid_coords[0]][grid_coords[1]-1]

                        # up
                        if up in neighbors:
                            up_neighbor_coords = (tile_to_modify['grid'][0], tile_to_modify['grid'][1])
                            neigh = self.hud.level.level_controller.get_neighbors(up_neighbor_coords)[0]
                            neigh_coords = (neigh['grid'][0], neigh['grid'][1])

                            if len(self.hud.level.level_controller.get_neighbors(neigh_coords)) == 3:
                                up['tile'] = "roadIntersectionUp"
                            elif len(self.hud.level.level_controller.get_neighbors(neigh_coords)) == 4:
                                up['tile'] = "roadIntersectionCenter"
                            
                            if up['tile'] == "roadLeft":
                                up['tile'] = "roadUpNextToLeft"

                            if up['tile'] == "roadRight":
                                up['tile'] = "roadUpNextToRight"
                            
                            tile_to_modify['tile'] = "roadUp"
                        # down
                        elif down in neighbors:
                            down_neighbor_coords = (tile_to_modify['grid'][0], tile_to_modify['grid'][1])
                            neigh = self.hud.level.level_controller.get_neighbors(down_neighbor_coords)[0]
                            neigh_coords = (neigh['grid'][0], neigh['grid'][1])

                            if len(self.hud.level.level_controller.get_neighbors(neigh_coords)) == 3:
                                down['tile'] = "roadIntersectionDown"
                            elif len(self.hud.level.level_controller.get_neighbors(neigh_coords)) == 4:
                                down['tile'] = "roadIntersectionCenter"

                            if down['tile'] == "roadLeft":
                                down['tile'] = "roadDownNextToLeft"

                            if down['tile'] == "roadRight":
                                down['tile'] = "roadDownNextToRight"

                            tile_to_modify['tile'] = "roadDown"
                        # left
                        elif left in neighbors:
                            left_neighbor_coords = (tile_to_modify['grid'][0], tile_to_modify['grid'][1])
                            neigh = self.hud.level.level_controller.get_neighbors(left_neighbor_coords)[0]
                            neigh_coords = (neigh['grid'][0], neigh['grid'][1])

                            if len(self.hud.level.level_controller.get_neighbors(neigh_coords)) == 3:
                                left['tile'] = "roadIntersectionLeft"
                            elif len(self.hud.level.level_controller.get_neighbors(neigh_coords)) == 4:
                                left['tile'] = "roadIntersectionCenter"
                                
                            if left['tile'] == "roadUp":
                                left['tile'] = "roadLeftNextToUp"

                            if left['tile'] == "roadDown":
                                left['tile'] = "roadLeftNextToDown"

                            tile_to_modify['tile'] = "roadLeft"
                        # right
                        elif right in neighbors:
                            right_neighbor_coords = (tile_to_modify['grid'][0], tile_to_modify['grid'][1])
                            neigh = self.hud.level.level_controller.get_neighbors(right_neighbor_coords)[0]
                            neigh_coords = (neigh['grid'][0], neigh['grid'][1])

                            if len(self.hud.level.level_controller.get_neighbors(neigh_coords)) == 3:
                                right['tile'] = "roadIntersectionRight"
                            elif len(self.hud.level.level_controller.get_neighbors(neigh_coords)) == 4:
                                right['tile'] = "roadIntersectionCenter"

                            if right['tile'] == "roadUp":
                                right['tile'] = "roadRightNextToUp"

                            if right['tile'] == "roadDown":
                                right['tile'] = "roadRightNextToDown"                          
                            
                            tile_to_modify['tile'] = "roadRight"
                        # default
                        else:
                            tile_to_modify['tile'] = "roadIntersectionCenter"
        
        """
        