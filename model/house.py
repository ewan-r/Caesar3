class House:
    #House Class to create
    def __init__(self,x,y,state,level):
        self.x = x
        self.y = y
        self.state = state
        self.level = 0
        self.collapseCounter = 0
        self.citizens = 0