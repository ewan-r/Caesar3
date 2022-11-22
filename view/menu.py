import pygame as pg
from pygame.locals import *

from controller.menu_controller import MenuController
from view.button import Button
from controller.button_controller import ButtonController

class Menu():
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

    def display_menu(self):
        """Display the game menu."""

        pg.init()

        pg.display.set_caption("INSA_lubrityIII")

        #pg.transform.scale(self.background, (self.window.get_size()))

        # controllers
        btn_controller = ButtonController(self)
        menu_controller = MenuController(self)

        # menu buttons
        self.buttons = []
        self.buttons.append(Button(pg.Rect(self.window.get_size()[0]/2-150, 150, 300, 50), "Start a new career", btn_controller.start_game))
        self.buttons.append(Button(pg.Rect(self.window.get_size()[0]/2-150, 225, 300, 50), "Load saved game", btn_controller.load_save))
        self.buttons.append(Button(pg.Rect(self.window.get_size()[0]/2-150, 300, 300, 50), "Exit", btn_controller.quit_game))
        
        btn_clicked = False
        loop = 1
        while loop:          
            for event in pg.event.get():
                if event.type == QUIT:
                    loop = 0
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
                               btn.ftn_click()
                               btn_clicked = True
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
                btn_controller.hover(btn)
                
            # clear the menu if a button is clicked
            if btn_clicked == True:
                menu_controller.clear()
            
            pg.display.update()    