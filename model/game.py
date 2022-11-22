from model.camera import Camera
from view.level import Level

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.entities = []

        self.level = Level(self.entities, 40, 40, self.width, self.height)
        
        # camera
        self.camera = Camera(self.width, self.height)