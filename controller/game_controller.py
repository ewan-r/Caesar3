from controller.aqueduc_controller import Aqueduc_Controller
import pygame as pg
import sys

from controller.camera_controller import CameraController
from controller.hud_button_controller import HUDButtonController
from view.button import Button
from model.storage import Storage
from view.pause_menu import PauseMenu

class GameController:
    """A GameController."""

    def __init__(self, game):
        """GameController constructor.
        
        Argument:
            game -- game to control
        """
        self.game = game
        self.economy_cooldown = 0
        self.playing = False
        self.screen = self.game.screen
        self.width, self.height = pg.display.get_surface().get_size()
        self.pause_menu = PauseMenu(self.screen, "")

        self.aqueduc_build_bool = False
        self.aqueduc_being_build = False
        self.aqueduc =[]
        self.aqueduc_cooldown = 0

        self.fctselected=False
        self.fct=""


    def run(self):
        """Run a game in a loop."""
        self.playing = True

        while self.playing:
            self.game.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        """Activate features during a game."""
        # controllers
        level_controller = self.game.level.level_controller
        hud_btn_controller = HUDButtonController(self.game.level.hud)
        camera_controller = CameraController(self.game.camera)
        x, y = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        grid_coords = level_controller.mouse_to_grid(x, y, camera_controller.camera.scroll)
        self.update_buildings(hud_btn_controller,level_controller.buildings) #Update buildings but we need level controller
        self.update_economy(hud_btn_controller,level_controller.economy_buildings)
        if (self.aqueduc_being_build):
            self.update_place_aqueducs(level_controller.level.preview_aqueduc, grid_coords)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    """Show the Pause Menu"""
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
                elif event.key == pg.K_RIGHT:
                    hud_btn_controller.create_farmBuilding(grid_coords,level_controller.economy_buildings)
                elif event.key == pg.K_a:
                    hud_btn_controller.create_granary(grid_coords,level_controller.economy_buildings)
                elif event.key == pg.K_z:
                    hud_btn_controller.create_reservoir(grid_coords,level_controller.economy_buildings)
                elif event.key == pg.K_w:
                    self.aqueduc_build_bool = True
                elif event.key == pg.K_c:
                    level_controller.level.preview_aqueduc.clear()
                    self.aqueduc_being_build = False
                    self.aqueduc_build_bool = False
                elif event.key == pg.K_p:
                    self.aqueduc[0].place_aqueduc(level_controller.level.preview_aqueduc)
                    level_controller.level.preview_aqueduc.clear()
                    self.aqueduc_being_build = False
                    self.aqueduc_build_bool = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for btn in self.game.level.hud.buttons:
                        if btn.rect.collidepoint(event.pos):
                            self.fct= btn.ftn_click
                            self.fctselected = True
        if click[0] and (self.aqueduc_build_bool == False) and (self.fctselected==True):
            if self.fct=="create_house":
                hud_btn_controller.create_house(grid_coords,level_controller.buildings)
            elif self.fct=="create_road":
                hud_btn_controller.create_road(grid_coords)
            elif self.fct=="engineerPost":
                hud_btn_controller.create_engineerPost(grid_coords)
            elif self.fct=="unselected":
                self.fctselected=False


            """
        elif click[0] and self.aqueduc_build_bool:
            aqueduc_controller = Aqueduc_Controller(grid_coords[0],grid_coords[1],level_controller)
            #level_controller.level.preview_aqueduc.append(aqueduc_controller)
            self.aqueduc_being_build = True
            self.aqueduc.append(aqueduc_controller)
        elif click[1] and (self.aqueduc_being_build or self.aqueduc_build_bool):
            level_controller.level.preview_aqueduc.clear()
            self.aqueduc_being_build = False
            self.aqueduc_build_bool = False"""

        if click[2] and (self.fctselected==True) and (self.fct=="destruction"):
            mouse_pos = pg.mouse.get_pos()
            self.game.mouse_pos_hud = level_controller.mouse_to_grid(mouse_pos[0], mouse_pos[1], camera_controller.camera.scroll)
            if self.game.cmpt < 2:
                self.game.first_pos = self.game.mouse_pos_hud
                self.game.cmpt = 2
        else:
            if  self.game.mouse_pos_hud[0]> self.game.first_pos[0]:
                for x in range( self.game.first_pos[0],  self.game.mouse_pos_hud[0] + 1):
                    if  self.game.mouse_pos_hud[1] > self.game.first_pos[1]:
                        for y in range( self.game.first_pos[1],  self.game.mouse_pos_hud[1] + 1):
                            hud_btn_controller.destruction(x,y)
                    else:
                        for y in range( self.game.mouse_pos_hud[1],  self.game.first_pos[1] + 1):
                            hud_btn_controller.destruction(x,y)
            else:
                for x in range( self.game.mouse_pos_hud[0], self.game.first_pos[0]+1):
                    if  self.game.mouse_pos_hud[1] >  self.game.first_pos[1]:
                        for y in range( self.game.first_pos[1], self.game.mouse_pos_hud[1]+1):
                            hud_btn_controller.destruction(x,y)
                    else:
                        for y in range ( self.game.mouse_pos_hud[1], self.game.first_pos[1]+1):
                            hud_btn_controller.destruction(x,y)
            self.game.mouse_pos_hud = (0,0)
            self.game.cmpt = 1
            self.game.first_pos = (0,0)

    def update(self):
        """Update a game."""
        camera_controller = CameraController(self.game.camera)
        camera_controller.update()

    def draw(self):
        """Draw sprites of a game."""
        self.game.screen.fill((0, 0, 0))
        # level
        self.game.level.draw(self.game.screen, self.game.camera)
        # HUD
        self.game.level.hud.display_hud()

    def update_buildings(self, hud,buildings):
        self.aqueduc_cooldown += self.game.clock.get_time()
        #if self.aqueduc_cooldown > 1000:    
        hud.update(buildings)
        self.aqueduc_cooldown =  0

    def update_place_aqueducs(self,list_of_tiles,gridcoords):
        self.aqueduc[0].preview_aqueduc(gridcoords,list_of_tiles)
        
    def update_economy(self,hud,economy_buildings):
        self.economy_cooldown += self.game.clock.get_time()
        if self.economy_cooldown > 200:
            hud.update_economy(economy_buildings)
            self.economy_cooldown = 0