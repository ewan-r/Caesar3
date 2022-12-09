import copy


class Aqueduc_Controller:
    def __init__(self,init_x,init_y,level):
        self.init_x = init_x
        self.init_y = init_y
        self.level = level
        self.neighbors = []
    """
    Comment gérer les routes:
    dans le game_controller pour le moment il faut faire un event si c'est le cas on déclenche une fonction de création de route qui est activée
    dans cette fonction le click gauche va poser un point de départ puis le mouvement de la souris est récupéré à chaque update pour pouvoir 
    trouver la derniere tile
    """
    def place_aqueduc(self,list_of_tiles_to_place):
        for tile_to_place in list_of_tiles_to_place:
            x = tile_to_place["grid"][0]
            y = tile_to_place["grid"][1]
            tile = tile_to_place["tile"]
            level_tile = self.level.level.level[x][y]["type_tile"]
            if (level_tile == ""):
                self.level.level.level[x][y]["tile"] = tile
                self.level.level.level[x][y]["type_tile"] = "buildings"
        
    def update (self, level):
        pass


    def preview_aqueduc(self,gridcoords,list_previewed_aqueducs):

        if (len(list_previewed_aqueducs) >=1):
            
            if (tuple(list_previewed_aqueducs[len(list_previewed_aqueducs)-1]["grid"])!= gridcoords):
                tile_to_preview = copy.deepcopy(self.level.level.level[gridcoords[0]][gridcoords[1]])
                tile_to_preview["tile"] = "aqueducleftright"
                tile_to_preview["type_tile"] = "buildings"
                #print("appending")
                list_previewed_aqueducs.append(tile_to_preview)
                self.neighbors = []
                last_tile_previewed = list_previewed_aqueducs[-2]   
                real_neighbors = self.level.get_real_neighbors(last_tile_previewed,"aqueduc",self.level.level.level)
                for real_neighbor in real_neighbors:
                        position = self.level.get_position_fictive_neighbor(last_tile_previewed["grid"],real_neighbor)
                        if (position != "empty"):
                            self.neighbors.append(position)
                #print("Real positions")
                #print(self.neighbors)
                for previewed_tile in list_previewed_aqueducs:
                    if (len(list_previewed_aqueducs) >= 1 and gridcoords != previewed_tile["grid"]):
                         
                        fictive_neighbor = self.level.get_position_fictive_neighbor(last_tile_previewed["grid"],previewed_tile)
                        if (fictive_neighbor != "empty"):
                            self.neighbors.append(fictive_neighbor)
                #print("Neighbors : ")
                #print(self.neighbors)
                self.find_right_tile(last_tile_previewed,self.neighbors)
                self.neighbors = []
                for real_neighbor in real_neighbors: 
                    real_neighbors_of_neighbor = self.level.get_real_neighbors(real_neighbor,"aqueduc",self.level.level.level)
                    for neighbor_of_real_neighbor in real_neighbors_of_neighbor:
                        if neighbor_of_real_neighbor != real_neighbor:
                            position = self.level.get_position_fictive_neighbor(real_neighbor["grid"],neighbor_of_real_neighbor)
                            if (position != "empty"):
                                self.neighbors.append(position)
                    for previewed_tile in list_previewed_aqueducs:
                        if (len(list_previewed_aqueducs) >= 1 and gridcoords != previewed_tile["grid"]):
                            
                            fictive_neighbor = self.level.get_position_fictive_neighbor(real_neighbor["grid"],previewed_tile)
                            if (fictive_neighbor != "empty"):
                                self.neighbors.append(fictive_neighbor)
                    self.find_right_tile(real_neighbor,self.neighbors)

                
                
                        

        else:
            tile_to_preview = copy.deepcopy(self.level.level.level[gridcoords[0]][gridcoords[1]])
            tile_to_preview["tile"] = "aqueducleftright"
            tile_to_preview["type_tile"] = "buildings"
            list_previewed_aqueducs.append(tile_to_preview)
        

            


    def find_right_tile(self,tile_to_change, neighbors):

        #print("Tile to change :")
        #print(" ")
        #print(tile_to_change)
        if (len(neighbors) >= 1):
            up = ""
            down =""
            right = ""
            left = ""
            isUp = False
            isDown = False
            isRight = False
            isLeft = False
            if ("up" in neighbors):
                up = "up"
                isUp = True
            if ("down" in neighbors):
                down = "down"
                isDown = True
            if ("right" in neighbors):
                right = "right"
                isRight = True
            if ("left" in neighbors):
                left = "left"
                isLeft = False
            if (isUp or isDown or isRight or isLeft):
                tile_to_change["tile"] = "aqueduc"+left+right+up+down
                tile_to_change["type_tile"] = "buildings"