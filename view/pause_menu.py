import pygame as pg
from pygame.locals import *
import time

from view.new_button import NewButton
from view.input_field import TextField

class PauseMenu():
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

    def display_menu(self):
        """Display the game menu."""

        pg.init()

        pg.display.set_caption("INSA_lubrityIII")

        #pg.transform.scale(self.background, (self.window.get_size()))

        pg.draw.rect(self.window, (100, 100, 100), (self.window.get_size()[0]/2-155, 120, 310, 325))
        # menu buttons
        self.buttons = []
        self.buttons.append(NewButton(pg.Rect(self.window.get_size()[0]/2-150, 150, 300, 50), "Continue", self.window))
        self.buttons.append(NewButton(pg.Rect(self.window.get_size()[0]/2-150, 225, 300, 50), "Load saved game", self.window))
        self.buttons.append(NewButton(pg.Rect(self.window.get_size()[0]/2-150, 300, 300, 50), "Save game", self.window))
        self.buttons.append(NewButton(pg.Rect(self.window.get_size()[0]/2-150, 375, 300, 50), "Exit to Main Menu", self.window))
          
        btn_clicked = False
        loop = 1
        while loop:          
            for event in pg.event.get():
                if event.type == QUIT:
                    loop = 0
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return
                # handle any other surfaces we might want to resize
                elif event.type == VIDEORESIZE: 
                    self.window.blit(pg.transform.scale(self.background, event.dict['size']), (0, 0))
                # handle parts of the window which need to be redrawn
                elif event.type == VIDEOEXPOSE:
                    self.window.blit(pg.transform.scale(self.background, self.window.get_size()), (0, 0))
                # buttons clicked
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for btn in self.buttons:
                            if btn.rect.collidepoint(event.pos):
                            # return a string corresponding to the command 
                               return btn.getCommand() 
                # buttons hovered
                elif event.type == pg.MOUSEMOTION:
                    for btn in self.buttons:
                        if btn.rect.collidepoint(event.pos):
                            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)  
                            break
                        else:
                            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)  

            # activate hover effect
            for btn in self.buttons:
                 btn.hover(btn)
            
            pg.display.update()    


    def save(self):
        # create object input_field
        filename_input = TextField(self.window, self.window.get_size()[0]/2-120, 200, 140, 32)
       
        self.buttons_save = []
        self.buttons_save.append(NewButton(pg.Rect(self.window.get_size()[0]/2-120, 300, 80, 50), "Save", self.window))
        self.buttons_save.append(NewButton(pg.Rect(self.window.get_size()[0]/2+40, 300, 80, 50), "Cancel", self.window))
       
        # passing Save & Cancel buttons as params to the input field
        return filename_input.render_window(self.buttons_save)
        