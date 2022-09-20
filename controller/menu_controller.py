import pygame

class MenuController():
    """A MenuController."""  

    def __init__(self, menu):
        """MenuController constructor.
        
        Argument:
            menu -- menu to be updated
        """
        self.menu = menu

    def clear(self):
        """Clear the game menu."""
        # cursor by default
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  
        self.menu.window.fill((0, 0, 0))
        self.menu.buttons.clear()