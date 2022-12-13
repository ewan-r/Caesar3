from model.camera import Camera
from view.level import Level

class Game:
    """A Game."""

    def __init__(self, menu, clock):
        """Game constructor.
        
        Arguments:
            screen -- screen to display a game
            clock -- game clock
        """
        self.menu = menu
        self.screen = self.menu.window
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.entities = []

        self.level = Level(self.entities, 40, 40, self.width, self.height)

        # camera
        self.camera = Camera(self.width, self.height)

        self.first_pos = (0,0)
        self.cmpt = 1
        self.mouse_pos_hud = (0,0)