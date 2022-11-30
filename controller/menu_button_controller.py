import pygame as pg
import sys

from model.game import Game
from controller.game_controller import GameController

class MenuButtonController():
    """A MenuButtonController."""  

    def __init__(self, menu):
        """MenuButtonController constructor.
        
        Argument:
            menu -- menu to be updated
        """
        self.menu = menu

    def start_game(self):
        """Start a game."""
        # put the window in fullscreen mode
        self.menu.window = pg.display.set_mode((1360, 765))

        game = Game(self.menu.window, pg.time.Clock())
        game_controller = GameController(game)
        game_controller.run()
        
    def load_save(self):
        """Load a save."""
        pass
    
    def quit_game(self):
        """Quit a game."""
        sys.exit()