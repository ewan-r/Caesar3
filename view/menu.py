import pygame
from pygame.locals import *
from view.button import Button
from controller.button_controller import ButtonController

class Menu():
    """A Menu.

    Attributes:
        window: surface to display infomations
        background_image: relative path of the background image
    """

    def __init__(self, window, background_image):
        """Init Menu with a window and a background image."""
        self.window = window
        self.background = background_image

    def display_menu(self):
        """Display the game menu."""

        pygame.init()

        pygame.display.set_caption("INSA_lubrityIII")

        pygame.transform.scale(self.background, (self.window.get_size()))

        loop = 1
        while loop:
            for event in pygame.event.get():
                if event.type == QUIT:
                    loop = 0
                # handle any other surfaces we might want to resize
                elif event.type == VIDEORESIZE: 
                    self.window.blit(pygame.transform.scale(self.background, event.dict['size']), (0, 0))
                # handle parts of the window which need to be redrawn
                elif event.type == VIDEOEXPOSE:
                    self.window.blit(pygame.transform.scale(self.background, self.window.get_size()), (0, 0))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for btn in buttons:
                            if btn.rect.collidepoint(event.pos):
                                btn.ftn_click()

            # menu buttons
            buttons = []
            
            btn_controller = ButtonController()

            buttons.append(Button(pygame.Rect(self.window.get_size()[0]/2-150, 150, 300, 50), "Start a new career", 0)) # put the function
            buttons.append(Button(pygame.Rect(self.window.get_size()[0]/2-150, 225, 300, 50), "Load saved game", 0)) # put the function
            buttons.append(Button(pygame.Rect(self.window.get_size()[0]/2-150, 300, 300, 50), "Exit", btn_controller.quit_game))

            for btn in buttons:
                btn.draw(self.window)
                
            pygame.display.update()    