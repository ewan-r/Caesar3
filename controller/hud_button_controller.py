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
            building.update()
    
    def update_economy (self,economy_buildings):
        for eco_building in economy_buildings:
            eco_building.update()
    def create_engineerPost(self,grid_coords):

        engineerPost = EngineerPost(grid_coords[0],grid_coords[1])
        if self.hud.level.level[engineerPost.x][engineerPost.y]['tile'] == "":
            engineerPostController = EngineerPost_Controller(engineerPost,self.hud)
            engineerPostController.place_post()
            #self.buildings.append(engineerPostController)
    def create_granary (self,gridcoords,buildings):
        granary = Granary(gridcoords[0],gridcoords[1],"normal")
        granaryController = Granary_Controller(granary, self.hud)
        granaryController.place_granary()
        buildings.append(granaryController)

    def create_reservoir (self, gridcoords, buildings):
        reservoir = Reservoir(gridcoords[0],gridcoords[1],"empty",-5)
        reservoirController = Reservoir_Controller(self.hud, reservoir)
        reservoirController.place_reservoir()
        buildings.append(reservoirController)

    def create_farmBuilding(self,grid_coords,buildings):
        farm = Farm(grid_coords[0],grid_coords[1],0,"normal")
        #if self.hud.level.level[farm.x][farm.y]['tile'] == "landFarm1":
        farmController = Farm_Controller(self.hud,farm)
        farmController.place_farm()
        buildings.append(farmController)
        #buildings.append(farmController)



    def create_house(self,grid_coords,buildings):

        house = House(grid_coords[0],grid_coords[1],"normal",1)
        if self.hud.level.level[house.x][house.y]['tile'] == "":
            houseController = HouseController(house,self.hud)
            houseController.place_house()
            buildings.append(houseController)

    def create_road(self, grid_coords):
        """Create a road.
        
        Argument:
            grid_coords -- grid coordinates of a cell
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