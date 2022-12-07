import pygame as pg
from pygame.locals import *
from view.button import Button
from view.input_field import TextField

class LoadMenu():
    """A Menu."""

    def __init__(self, window, background_image):
        """Menu constructor.
        
        Arguments:
            window -- surface to display infomations
            background_image -- relative path of the background image
        """
        self.window = window
        self.background = background_image
        self.buttons = []
    
    def clear(self):
        """Clear the game menu."""
        # cursor by default
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)  
        #self.menu.window.fill((0, 0, 0))
        self.buttons.clear()

    def loading_name(self):
        """Display the game menu."""

        # calling the Input field
        command = self.load_field()
        if(command[0] == "Load"):
            return command[1]
        else:
            exit(0)


    def load_field(self):
        # create object input_field
        filename_input = TextField("load",self.window, self.window.get_size()[0]/2-120, 200, 140, 32)
                
        self.buttons_save = []
        self.buttons_save.append(Button(pg.Rect(self.window.get_size()[0]/2-120, 350, 80, 50), "Load"))
        self.buttons_save.append(Button(pg.Rect(self.window.get_size()[0]/2+40, 350, 80, 50), "Cancel"))
        
        # passing Save & Cancel buttons as params to the input field
        return filename_input.render_window(self.buttons_save)