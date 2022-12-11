#! /usr/bin/env python3

import pygame as pg
from pygame.locals import *
from controller.menu_button_controller import MenuButtonController

from view.menu import Menu

def main():
    """Main program."""
    # the window is resizable and it is possible to put it in fullscreen
    window = pg.display.set_mode((0,0), pg.FULLSCREEN)
    # relative path of the background image
    background_image = pg.image.load("assets/background/insa-lubrityiii-bg.png").convert_alpha()

    game_menu = Menu(window, background_image)

    menu_btn_controller = MenuButtonController(game_menu)
    command_response = game_menu.display_menu()
    command = command_response[0]

    if command == "Start a new career":
        menu_btn_controller.start_game()
    elif command == "Load saved game":
        menu_btn_controller.load_save()
    elif command == "Exit":
        menu_btn_controller.quit_game()
    
if __name__ == "__main__":
    main()