import pygame
import sys

class ButtonController():
    """A ButtonController."""  

    def __init__(self):
        """Init ButtonController."""
        pass  

    def hover(self, window, btn):
        """Modify the border radius of a button when the mouse hover it."""
        is_hovered = False

        if btn.rect.collidepoint(pygame.mouse.get_pos()):
            is_hovered = True
            btn.draw(window, is_hovered)
        else:
            btn.draw(window, is_hovered)

    def start_game(self):
        """Start a game."""
        pass

    def load_save(self):
        """Load a save."""
        pass
    
    def quit_game(self):
        """Quit a game."""
        sys.exit()