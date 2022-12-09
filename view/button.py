import pygame as pg
from pygame.locals import *

class Button():
    """A Button."""
    
    def __init__(self, rect, command_name):
        """Button constructor.

        Arguments:
            rect -- rectangle of the button ordinate
            text -- signification of the button
            ftn_click -- function executed when the button is clicked
        """
        self.rect = rect
        self.command_name = command_name
        self.command_response = [] 
        self.command_response.append(self.command_name) # 1's element is command name, 2nd is a message

    def get_command(self):
        return self.command_response
    
    def append_message(self, msg):
        self.command_response.append(msg)

    def hover(self, window, btn, type_menu):
        """Modify the border radius of a button when the mouse hover it.
        
        Argument:
            window --
            btn -- button on which the border radius is changed
            type_menu --
        """
        is_hovered = False

        if btn.rect.collidepoint(pg.mouse.get_pos()):
            is_hovered = True
            btn.draw(window, is_hovered, type_menu)
        else:
            btn.draw(window, is_hovered, type_menu)

    def draw(self, window, is_hovered, type_menu):
        """Draw a rectangle representing a button.
        
        Arguments:
            window -- surface to display infomations
            is_hovered -- True if the button is hovered, False if it isn't
            type_menu -- menu string
        """
        if is_hovered == False:
            font = pg.font.Font("assets/font/Forum-Regular.ttf", 25)
            text = font.render(self.command_name, 1, (0,0,0))

            # Menu, Pause Menu
            if (type_menu == "Menu" or type_menu == "Pause Menu"):
                pg.draw.rect(window, (149, 148, 116), self.rect, 0, 2, 2)
            # HUD
            elif (type_menu == "HUD"):
                text = font.render("", 1, (0,0,0))
                transparent_surface = pg.Surface((0, 0), pg.SRCALPHA)
                pg.draw.rect(transparent_surface, (0, 22, 0, 0), self.rect, 0, 0)
            
            # put the text at the center of the button
            window.blit(text, (self.rect.x + (self.rect.width/2 - text.get_width()/2), self.rect.y + (self.rect.height/2 - text.get_height()/2)))
        else:            
            pg.draw.rect(window, (0, 0, 0), self.rect, 2, 2)