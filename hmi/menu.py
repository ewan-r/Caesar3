#! /usr/bin/env python3

import pygame
from pygame.locals import *

class Menu():
    """A Menu.

    Attributes:
        window: surface to display infomations
        background_image: relative path of the background image
    """

    # dimensions of the basic window
    window_width = 1600
    window_height = 900

    def __init__(self, window, background_image):
        """Init Menu with a window and a background image."""
        self.window = window
        self.background = background_image

    def display_menu(self):
        """Display the game menu."""

        pygame.init()

        pygame.display.set_caption("Caesar III")

        pygame.transform.scale(self.background, (self.window.get_size()))

        loop = 1
        while loop:
            # start Pygame event handlers
            pygame.event.pump()
            # wait for a single event from the queue
            event = pygame.event.wait()

            if event.type == QUIT:
                loop = 0
            # handle any other surfaces we might want to resize
            elif event.type == VIDEORESIZE: 
                self.window.blit(pygame.transform.scale(self.background, event.dict['size']), (0, 0))
                pygame.display.update()
            # handle parts of the window which need to be redrawn
            elif event.type == VIDEOEXPOSE:
                self.window.fill((0, 0, 0))
                self.window.blit(pygame.transform.scale(self.background, self.window.get_size()), (0, 0))            
                pygame.display.update()


def main():
    # the window is resizable and it is possible to put it in fullscreen
    window = pygame.display.set_mode((Menu.window_width, Menu.window_height), RESIZABLE, FULLSCREEN)
    # relative path of the background image
    background_image = pygame.image.load("data/img/caesar3-bg.png")

    game_menu = Menu(window, background_image)
    game_menu.display_menu()

main()