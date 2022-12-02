class Reservoir_Controller:
    def __init__ (self,hud,reservoir):
        self.hud = hud
        self.reservoir = reservoir
        self.level = self.hud.level.level 
        self.tile_to_modify = self.hud.level.level[reservoir.x][reservoir.y]
        self.water_placement = self.hud.level.level[reservoir.x-2][reservoir.y - 3]
        self.is_there_water = False
        self.index_of_animation = 35
        self.network = []
        self.reservoir.water_entrance_coords = self.get_water_entrance_tiles_coords()
    def place_reservoir (self):
        self.attach_building_to_tiles()
        self.tile_to_modify["tile"] = "reservoir34"
        self.tile_to_modify["type_tile"] = "buildings"
        if (self.is_There_Water()):
            self.reservoir.status = "full"
       

    def is_There_Water(self):
        for x in range (self.reservoir.x - 5, self.reservoir.x + 5):
            for y in range (self.reservoir.y - 5, self.reservoir.y+5):
                if (self.hud.level.level[x][y]["type_tile"] == "landsWater" ):
                    return True
        return False

    def update_tile_water(self):
        self.water_placement["tile"] = "reservoir"+str(self.index_of_animation)
        self.water_placement["type_tile"] = "buildings"


    def update(self):
        if(self.reservoir.status == "empty"):
            self.get_path_of_aqueduc()
        #print(self.reservoir.status)
        if (self.reservoir.status == "full"):
            self.water_placement["tile"] = "reservoir35"
            self.water_placement["type_tile"] = "buildings"
            """if (self.index_of_animation < 42):
                self.update_tile_water()
                self.index_of_animation +=1
            else:
                self.index_of_animation = 35"""
            #We change tile in reservoir in order to display that it is full
            #self.water_placement["tile"] = "reservoir35"
            #self.water_placement["type_tile"] = "buildings"
            #It works but we need to blit it after the reservoir in order to display over the reservoir
    def attach_building_to_tiles (self):
        for coord in self.reservoir.tiles_coords :
            self.level[coord[0]][coord[1]]["attached_to_building"] = ["reservoir",self.reservoir.x,self.reservoir.y]
            #print(self.level[coord[0]][coord[1]])
    def get_water_entrance_tiles_coords(self):
        """This function returns an array of coordinates of tiles where water can be connected to the reservoir

        Returns:
            list: List of lists of coords (x,y)
        """
        x = self.reservoir.x
        y = self.reservoir.y
        water_entry1 = [x+1,y-1]
        water_entry2 = [x-1,y-3]
        water_entry3 = [x-3,y-1]
        water_entry4 = [x-1,y+1]

        return [water_entry1, water_entry2, water_entry3, water_entry4]
    def get_water_tiles(self):
        tiles = []
        for coords in self.reservoir.water_entrance_coords:
          tiles.append(self.level[coords[0]][coords[1]])
        return tiles  


    def get_path_of_aqueduc (self):
        for network in self.get_water_tiles():
            self.network.clear()
            self.get_list_of_aqueduc_network(network)
            if (self.is_linked_to_another_reservoir(self.network)):
                self.reservoir.status = "full"
    """
    print("---------------------")
        print("Water entrance tiles :")
        print(self.get_water_tiles())
        print("---------------------")
        if (self.is_there_water == False):
            if (self.is_linked_to_another_reservoir(self.get_water_tiles(), self.water_placement)):
                self.reservoir.status = "full"
    Comment faire pour savoir si on a relié deux résevoirs entre eux avec des aqueducs ? 
    - on parcourt tous les voisins qui sont des aqueducs et on regardes de manière récursive
    """

    def is_linked_to_another_reservoir(self, list_tiles):
        for next_tile in list_tiles:
            neighbors = self.is_building_nearby(next_tile,"reservoir",self.hud.level.level)
            for neighbor in neighbors:
                if ([self.reservoir.x, self.reservoir.y ]!= [neighbor["attached_to_building"][1],neighbor["attached_to_building"][2]]):
                    return True
        return False      

    def get_list_of_aqueduc_network(self, starting_point):
        list_of_nearby_aqueducs = self.get_real_neighbors(starting_point, "aqueduc", self.hud.level.level)
        for next_aqueduc in list_of_nearby_aqueducs:
            if next_aqueduc not in self.network:
                self.network.append(next_aqueduc)
                self.get_list_of_aqueduc_network(next_aqueduc)
                #print(self.network)
                print(len(self.network))

    
    def is_building_nearby (self, tile, building, level):
        #print ("--------------------")
        #print("Printing tile grid in building nearby :")
        #print(tile['grid'])

        x = tile['grid'][0]
        y = tile['grid'][1]
        neighbors = []

        if ( building in level[x-1][y]["attached_to_building"]):
            neighbors.append(level[x-1][y])
        if (building in level[x+1][y]["attached_to_building"]):
            neighbors.append(level[x+1][y])
        if (building in level[x][y-1]["attached_to_building"]):
            neighbors.append(level[x][y-1])
        if (building in level[x][y+1]["attached_to_building"]):
            neighbors.append(level[x][y+1])
        return neighbors
        
    def get_real_neighbors (self, tile_to_get_neighors_from,type_tile_world, level):
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



    def fill_aqueducs_nearby (self):
        for water_entrance in self.get_water_tiles():
            if "aqueduc" in water_entrance :
                pass
    """
    Comment faire pour que le système de liaison d'eau soit efficace ?
    Ce que l'on attend : 
    Un rés a côté d'une source d'eau aliment des aqueducs qui acheminent l'eau jusqu'à d'autres résevoirs
    eux même peuvent acheminer de l'eau mais si par exemple la première laison est coupée 
    alors le système ne se suffit plus.

    """