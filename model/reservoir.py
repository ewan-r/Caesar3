
class Reservoir:
    def __init__(self,x,y,status,impact):
        self.x = x
        self.y = y
        self.status = status
        self.impact = impact
        self.tiles_coords = [(x+i,y+j) for i in range (3) for j in range (3)]
        self.water_entrance = []
