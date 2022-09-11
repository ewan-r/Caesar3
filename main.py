#! /usr/bin/env python3

import pygame
from pygame.locals import *
from view.menu import Menu

def main():
    """Main program."""
    # the window is resizable and it is possible to put it in fullscreen
    window = pygame.display.set_mode((1600, 900), RESIZABLE, FULLSCREEN)
    # relative path of the background image
    background_image = pygame.image.load("view/data/img/insa-lubrityiii-bg.png")

    game_menu = Menu(window, background_image)
    game_menu.display_menu()

if __name__ == "__main__":
    main()