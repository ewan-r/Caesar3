#! /usr/bin/env python3

import pygame as pg
from pygame.locals import *

from view.menu import Menu

def main():
    """Main program."""
    # the window is resizable and it is possible to put it in fullscreen
    window = pg.display.set_mode((1600, 900), RESIZABLE, FULLSCREEN)
    # relative path of the background image
    background_image = pg.image.load("assets/background/insa-lubrityiii-bg.png").convert_alpha()

    game_menu = Menu(window, background_image)
    game_menu.display_menu()
    
if __name__ == "__main__":
    main()