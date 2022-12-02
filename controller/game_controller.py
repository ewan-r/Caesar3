import pygame as pg
import sys

from controller.camera_controller import CameraController
from controller.hud_button_controller import HUDButtonController
from model.storage import Storage
from view.pause_menu import PauseMenu

class GameController:
    def __init__(self, game):
        self.game = game
        self.economy_cooldown = 0
        self.playing = False
        self.screen = self.game.screen
        self.width, self.height = pg.display.get_surface().get_size()
        self.pause_menu = PauseMenu(self.screen, "")

    def run(self):
        self.playing = True

        while self.playing:
            self.game.clock.tick(60)
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        # controllers
        level_controller = self.game.level.level_controller
        hud_btn_controller = HUDButtonController(self.game.level.hud)
        camera_controller = CameraController(self.game.camera)
        x, y = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        grid_coords = level_controller.mouse_to_grid(x, y, camera_controller.camera.scroll)
        self.update_buildings(hud_btn_controller,level_controller.buildings) #Update buildings but we need level controller
        self.update_economy(hud_btn_controller,level_controller.economy_buildings)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    '''
                    Show the Pause Menu
                    '''
                    commandResp = self.pause_menu.display_menu()
                    command = commandResp[0]
                    if (command == "Exit to Main Menu"):
                        pg.quit
                        sys.exit()
                    elif(command == "Continue"):
                        pass
                    elif(command == "Save game"):
                        commandResp2 = self.pause_menu.save()
                        command = commandResp2[0]
                        destination_file = commandResp2[1]
                        # if save Game option is selected from Pause Menu
                        if(command == "Cancel"):
                            pass
                        elif(command == "Save"):
                            gameData = Storage(self.game.level.level)
                            gameData.save_game(destination_file)

                    self.playing = True
                elif event.key == pg.K_LEFT:
                    hud_btn_controller.create_engineerPost(grid_coords)
                elif event.key == pg.K_RIGHT:
                    hud_btn_controller.create_farmBuilding(grid_coords,level_controller.economy_buildings)

        if click[0]:
            hud_btn_controller.create_house(grid_coords,level_controller.buildings)

    def update(self):
        camera_controller = CameraController(self.game.camera)
        camera_controller.update()

    def draw(self):
        self.game.screen.fill((0, 0, 0))
        self.game.level.draw(self.game.screen, self.game.camera)
        pg.display.flip()

    def update_buildings(self, hud,buildings):
        hud.update(buildings)

    def update_economy(self,hud,economy_buildings):
        self.economy_cooldown += self.game.clock.get_time()
        if self.economy_cooldown > 400:
            hud.update_economy(economy_buildings)
            self.economy_cooldown = 0
