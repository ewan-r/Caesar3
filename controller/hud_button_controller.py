from controller.reservoir_controller import Reservoir_Controller
from model.reservoir import Reservoir
from controller.granary_controller import Granary_Controller
from controller.farm_controller import Farm_Controller
from controller.engineerPost_controller import EngineerPost_Controller
from model.engineerpost import EngineerPost
from controller.house_controller import HouseController
from model.house import House
from model.farm import Farm
from model.granary import Granary

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

    def update(self,buildings):

        for building in buildings:
            building.update(buildings)
    
    def update_economy (self,economy_buildings):
        for eco_building in economy_buildings:
            eco_building.update()
    def create_engineerPost(self,grid_coords, employers_buildings, buildings, game):
        engineerPost = EngineerPost(grid_coords[0],grid_coords[1])
        if self.hud.level.level[engineerPost.x][engineerPost.y]['tile'] == "" and game.dinars > 20:
            engineerPostController = EngineerPost_Controller(engineerPost,self.hud)
            engineerPostController.place_post()
            employers_buildings.append(engineerPostController)
            buildings.append(engineerPostController)
            game.dinars -= 20
            #self.buildings.append(engineerPostController)
    def create_granary (self,gridcoords,buildings, game):
        if ((gridcoords[0] < 38 and gridcoords[0] > 1) and (gridcoords[1] < 38 and gridcoords[1] > 1)):
            granary = Granary(gridcoords[0],gridcoords[1],"normal")
            granaryController = Granary_Controller(granary, self.hud)
            if (all ([tile["tile"] == "" and tile["attached_to_building"] == [] for tile in granaryController.neighbors]) and game.dinars > 20):
                granaryController.place_granary()
                buildings.append(granaryController)
                game.dinars -= 20

    def create_reservoir (self, gridcoords, buildings):
        reservoir = Reservoir(gridcoords[0],gridcoords[1],"empty",-5)
        reservoirController = Reservoir_Controller(self.hud, reservoir)
        reservoirController.place_reservoir()
        buildings.append(reservoirController)

    def create_farmBuilding(self,grid_coords,buildings, employers_buildings, game):

        if ((grid_coords[0] < 39 and grid_coords[0] > 0) and (grid_coords[1] < 39 and grid_coords[1] > 0)):
            farm = Farm(grid_coords[0],grid_coords[1],0,"normal")
            #if self.hud.level.level[farm.x][farm.y]['tile'] == "landFarm1":
            farmController = Farm_Controller(self.hud,farm, game)
            if (all ([neighbor["tile"] == "landFarm1" and neighbor["attached_to_building"] == [] for neighbor in farmController.neighbors]) and game.dinars > 10):
                farmController.place_farm()
                buildings.append(farmController)
                employers_buildings.append(farmController)
                game.dinars -= 10

    def create_house(self,grid_coords,buildings, game):
        house = House(grid_coords[0],grid_coords[1],"normal",1)
        try :
            if self.hud.level.level[house.x][house.y]['tile'] == "" and game.dinars > 5:
                houseController = HouseController(house,self.hud, game)
                houseController.place_house()
                buildings.append(houseController)
                game.dinars -= 5
        except : 
            pass
    def create_road(self, click_pos, pos_mouse):
        """Create a road.
        
        Argument:
            grid_coords -- grid coordinates of a cell
        """
    
        if pos_mouse[0] < self.hud.level.grid_length_x and pos_mouse[1] < self.hud.level.grid_length_y:
            if pos_mouse[0] >= 0 and pos_mouse[1] >= 0:
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
                    
                        if tile_to_modify['type_tile'] == "" or tile_to_modify['type_tile'] == "landsRoad":
                            tile_to_modify['type_tile'] = "landsRoad"
                            neighbors_tile = self.hud.level.level_controller.get_neighbors_tile(tile_to_modify["grid"], "road")
                            self.hud.level.level_controller.find_right_tile(tile_to_modify, neighbors_tile, "road")

                            real_neighbors = self.hud.level.level_controller.get_real_neighbors(tile_to_modify, "road", self.hud.level.level)

                            for real_neighbor in real_neighbors:
                                neighbors_of_real_neighbor = self.hud.level.level_controller.get_neighbors_tile(real_neighbor["grid"], "road")
                                self.hud.level.level_controller.find_right_tile(real_neighbor, neighbors_of_real_neighbor, "road")

    def destruction(self, x,y):
        """Create a road.

        Argument:
            pos_sprite_to_modify -- position of the sprite where a route will be created
        """
        if x>0 and x<39 and y>0 and y<39:
            level_tile_to_modify = self.hud.level.level[x][y]

            if level_tile_to_modify["destructible"]:
                level_tile_to_modify['type_tile'] = "lands"
                level_tile_to_modify['tile'] = "land81"