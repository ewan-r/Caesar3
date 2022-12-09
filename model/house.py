class House:
    #House Class to create
    def __init__(self,x,y,state,level):
        self.x = x
        self.y = y
        self.state = state
        self.level = level
        self.collapseCounter = 0
        self.citizens = 0