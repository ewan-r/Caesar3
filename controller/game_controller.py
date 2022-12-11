import pygame as pg
import sys

from controller.aqueduc_controller import Aqueduc_Controller
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
        self.dinars = 0
        self.workers = 0
        self.free_workers = 0
        self.citizens = 0
        self.economy_cooldown = 0
        self.food = 2000
        self.playing = False
        self.screen = self.game.screen
        self.width, self.height = pg.display.get_surface().get_size()
        self.pause_menu = PauseMenu(self.screen, "")

        self.aqueduc_build_bool = False
        self.aqueduc_being_build = False
        self.aqueduc =[]
        self.aqueduc_cooldown = 0

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
        self.update_economy(hud_btn_controller,level_controller.economy_buildings, level_controller.employers_buildings)
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
                mouse_presses=pg.mouse.get_pressed()
                click = pg.mouse.get_pressed()
                if event.button == 1:
                    for btn in self.game.level.hud.buttons:
                        if btn.rect.collidepoint(event.pos) and (mouse_presses[0]):
                            self.game.level.hud.fct= btn.command_name
                            self.game.level.hud.fctselected = True
                    for subbtn in self.game.level.hud.subbuttons:
                        if subbtn.rect.collidepoint(event.pos) and (mouse_presses[0]):
                            self.game.level.hud.fct= subbtn.command_name
                            self.game.level.hud.subfctselected = True
                if mouse_presses[1] and (self.game.level.hud.fctselected == True):
                    if self.game.level.hud.fct == "unselected":
                        self.game.level.hud.subfctselected = False
                        self.game.level.hud.fctselected = False
                if mouse_presses[2] and (self.game.level.hud.fctselected==True):
                    if self.game.level.hud.fct=="engineerPost":
                        hud_btn_controller.create_engineerPost(grid_coords, level_controller.employers_buildings, level_controller.buildings, self)
                if mouse_presses[2] and (self.game.level.hud.fctselected == True) and (self.game.level.hud.subfctselected == True):
                    if self.game.level.hud.fct == "Reservoir":
                        hud_btn_controller.create_reservoir(grid_coords, level_controller.economy_buildings)
                    if self.game.level.hud.fct == "Granary":
                        hud_btn_controller.create_granary(grid_coords, level_controller.economy_buildings, self)
                    if self.game.level.hud.fct == "Farm":
                        hud_btn_controller.create_farmBuilding(grid_coords, level_controller.economy_buildings, level_controller.employers_buildings, self)
        if click[2] and (self.game.level.hud.fctselected==True):
            if self.game.level.hud.fct=="create_house":
                hud_btn_controller.create_house(grid_coords,level_controller.buildings, self)
            elif self.game.level.hud.fct=="create_road":
                click_x_pos_mouse, click_y_pos_mouse = pg.mouse.get_pos()
                click_pos = level_controller.mouse_to_grid(click_x_pos_mouse, click_y_pos_mouse, camera_controller.camera.scroll)
                
                hud_btn_controller.create_road(click_pos, grid_coords)

        if click[2] and (self.game.level.hud.fctselected==True) and (self.game.level.hud.subfctselected==True):
            #if self.game.level.hud.fct=="create_aqueduct":
                #hud_btn_controller.create_reservoir(grid_coords, level_controller.economy_buildings)

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

        if click[2] and (self.game.level.hud.fctselected==True) and (self.game.level.hud.fct=="destruction"):
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
        self.game.level.hud.display_hud(self.dinars, self.workers, self.citizens, self.food)
        # road button
        road_btn = Button(pg.Rect(1268, 299, 42, 29), "Create road")
        road_btn.hover(self.game.screen, road_btn, "HUD") 

    def update_buildings(self, hud,buildings):
        self.aqueduc_cooldown += self.game.clock.get_time()
        #if self.aqueduc_cooldown > 1000:    
        hud.update(buildings)
        self.aqueduc_cooldown =  0

    def update_place_aqueducs(self,list_of_tiles,gridcoords):
        self.aqueduc[0].preview_aqueduc(gridcoords,list_of_tiles)
        
    def update_economy(self,hud,economy_buildings, employers_buildings): 
        self.economy_cooldown += self.game.clock.get_time()
        if self.economy_cooldown > 200:
            self.dinars += 1
            self.workers = round (0.6 * self.citizens)
            self.free_workers = self.workers
            workers = [0] * len (employers_buildings)
            if (len(workers) >= 1):
                while (self.free_workers > 1):
                    for i in range (len(workers)):
                        if (self.free_workers > 0):
                            workers[i] +=1
                            self.free_workers -= 1
            for building_index in range (len(employers_buildings)):
                employers_buildings[building_index].workers = workers[building_index] 

            hud.update_economy(economy_buildings)
            self.economy_cooldown = 0