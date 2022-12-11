import pygame as pg
import sys

from model.game import Game
from model.storage import Storage
from controller.game_controller import GameController
from view.load_menu import LoadMenu

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
        game = Game(self.menu.window, pg.time.Clock())
        game_controller = GameController(game)

        game_controller.run()
        
        
    def load_save(self):
        """Load a saved game."""
        load_game = LoadMenu(self.menu.window,"")
        filename = load_game.loading_name()
      
        self.menu.window = pg.display.set_mode((1360, 765))
        game = Game(self.menu.window, pg.time.Clock())
        stored_level = Storage([])

        # replacing default world with a saved world
        game.level.level = stored_level.restore_world(filename + ".bin")

        game_controller = GameController(game)
        game_controller.run()

    def quit_game(self):
        """Quit a game."""
        sys.exit()