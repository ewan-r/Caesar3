import pygame as pg
import sys

from model.game import Game

class ButtonController():
    """A ButtonController."""  

    def __init__(self, menu):
        """ButtonController constructor.
        
        Argument:
            menu -- menu to be updated
        """
        self.menu = menu

    def hover(self, btn):
        """Modify the border radius of a button when the mouse hover it.
        
        Argument:
            btn -- button on which the border radius is changed
        """
        is_hovered = False

        if btn.rect.collidepoint(pg.mouse.get_pos()):
            is_hovered = True
            btn.draw(self.menu.window, is_hovered)
        else:
            btn.draw(self.menu.window, is_hovered)

    def start_game(self):
        """Start a game."""
        game = Game(self.menu.window, pg.time.Clock())

        game.run()
        
    def load_save(self):
        """Load a save."""
        pass
    
    def quit_game(self):
        """Quit a game."""
        sys.exit()