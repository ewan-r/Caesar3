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
                    
                    neighbors = self.hud.level.level_controller.get_path(grid_coords)

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
                            neigh = self.hud.level.level_controller.get_path(up_neighbor_coords)[0]
                            neigh_coords = (neigh['grid'][0], neigh['grid'][1])

                            if len(self.hud.level.level_controller.get_path(neigh_coords)) == 3:
                                up['tile'] = "roadIntersectionUp"
                            elif len(self.hud.level.level_controller.get_path(neigh_coords)) == 4:
                                up['tile'] = "roadIntersectionCenter"
                            
                            if up['tile'] == "roadLeft":
                                up['tile'] = "roadUpNextToLeft"

                            if up['tile'] == "roadRight":
                                up['tile'] = "roadUpNextToRight"
                            
                            tile_to_modify['tile'] = "roadUp"
                        # down
                        elif down in neighbors:
                            down_neighbor_coords = (tile_to_modify['grid'][0], tile_to_modify['grid'][1])
                            neigh = self.hud.level.level_controller.get_path(down_neighbor_coords)[0]
                            neigh_coords = (neigh['grid'][0], neigh['grid'][1])

                            if len(self.hud.level.level_controller.get_path(neigh_coords)) == 3:
                                down['tile'] = "roadIntersectionDown"
                            elif len(self.hud.level.level_controller.get_path(neigh_coords)) == 4:
                                down['tile'] = "roadIntersectionCenter"

                            if down['tile'] == "roadLeft":
                                down['tile'] = "roadDownNextToLeft"

                            if down['tile'] == "roadRight":
                                down['tile'] = "roadDownNextToRight"

                            tile_to_modify['tile'] = "roadDown"
                        # left
                        elif left in neighbors:
                            left_neighbor_coords = (tile_to_modify['grid'][0], tile_to_modify['grid'][1])
                            neigh = self.hud.level.level_controller.get_path(left_neighbor_coords)[0]
                            neigh_coords = (neigh['grid'][0], neigh['grid'][1])

                            if len(self.hud.level.level_controller.get_path(neigh_coords)) == 3:
                                left['tile'] = "roadIntersectionLeft"
                            elif len(self.hud.level.level_controller.get_path(neigh_coords)) == 4:
                                left['tile'] = "roadIntersectionCenter"
                                
                            if left['tile'] == "roadUp":
                                left['tile'] = "roadLeftNextToUp"

                            if left['tile'] == "roadDown":
                                left['tile'] = "roadLeftNextToDown"

                            tile_to_modify['tile'] = "roadLeft"
                        # right
                        elif right in neighbors:
                            right_neighbor_coords = (tile_to_modify['grid'][0], tile_to_modify['grid'][1])
                            neigh = self.hud.level.level_controller.get_path(right_neighbor_coords)[0]
                            neigh_coords = (neigh['grid'][0], neigh['grid'][1])

                            if len(self.hud.level.level_controller.get_path(neigh_coords)) == 3:
                                right['tile'] = "roadIntersectionRight"
                            elif len(self.hud.level.level_controller.get_path(neigh_coords)) == 4:
                                right['tile'] = "roadIntersectionCenter"

                            if right['tile'] == "roadUp":
                                right['tile'] = "roadRightNextToUp"

                            if right['tile'] == "roadDown":
                                right['tile'] = "roadRightNextToDown"                          
                            
                            tile_to_modify['tile'] = "roadRight"
                        # default
                        else:
                            tile_to_modify['tile'] = "roadIntersectionCenter"
                            
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