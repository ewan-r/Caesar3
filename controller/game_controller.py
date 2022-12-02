from controller.aqueduc_controller import Aqueduc_Controller
import pygame as pg
import sys

from controller.camera_controller import CameraController
from controller.hud_button_controller import HUDButtonController

class GameController:
    def __init__(self, game):
        self.game = game
        self.economy_cooldown = 0
        self.aqueduc_build_bool = False
        self.aqueduc_being_build = False
        self.aqueduc =[]
        self.aqueduc_cooldown = 0
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
        self.update_buildings(hud_btn_controller,level_controller.buildings,grid_coords) #Update buildings but we need level controller
        self.update_economy(hud_btn_controller,level_controller.economy_buildings)
        if (self.aqueduc_being_build):
            self.update_place_aqueducs(level_controller.level.preview_aqueduc, grid_coords)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_LEFT:
                    hud_btn_controller.create_engineerPost(grid_coords)
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
        if click[0] and (self.aqueduc_build_bool == False):
            hud_btn_controller.create_house(grid_coords,level_controller.buildings)
        elif click[0] and self.aqueduc_build_bool:
            aqueduc_controller = Aqueduc_Controller(grid_coords[0],grid_coords[1],level_controller)
            #level_controller.level.preview_aqueduc.append(aqueduc_controller)
            self.aqueduc_being_build = True
            self.aqueduc.append(aqueduc_controller)
    

        
        elif click[1] and (self.aqueduc_being_build or self.aqueduc_build_bool):
            level_controller.level.preview_aqueduc.clear()
            self.aqueduc_being_build = False
            self.aqueduc_build_bool = False

    def update(self):
        camera_controller = CameraController(self.game.camera)
        camera_controller.update()

    def draw(self):
        self.game.screen.fill((0, 0, 0))
        self.game.level.draw(self.game.screen, self.game.camera)
        pg.display.flip()

    def update_buildings(self, hud,buildings,gridcoords):
        hud.update(buildings)

    def update_place_aqueducs(self,list_of_tiles,gridcoords):
        self.aqueduc_cooldown += self.game.clock.get_time()
        self.aqueduc[0].preview_aqueduc(gridcoords,list_of_tiles)
        self.aqueduc_cooldown =  0

    def update_economy(self,hud,economy_buildings):
        self.economy_cooldown += self.game.clock.get_time()
        if self.economy_cooldown > 200:
            hud.update_economy(economy_buildings)
            self.economy_cooldown = 0
