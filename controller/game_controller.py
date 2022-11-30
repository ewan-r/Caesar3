import pygame as pg
import sys

from controller.camera_controller import CameraController
from controller.hud_button_controller import HUDButtonController
from view.button import Button

class GameController:
    def __init__(self, game):
        self.game = game

        self.first_pos = (0,0)
        self.cmpt = 1
        self.mouse_pos_hud = (0,0)

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

        btn_clicked = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                btn_clicked = True

        x, y = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        grid_coords = level_controller.mouse_to_grid(x, y, camera_controller.camera.scroll)

        if click[0]:
            hud_btn_controller.create_road(grid_coords)
        if click[2]:
            mouse_pos = pg.mouse.get_pos()
            self.mouse_pos_hud = level_controller.mouse_to_grid(mouse_pos[0], mouse_pos[1], camera_controller.camera.scroll)
            if  self.cmpt < 2:
                self.first_pos =  self.mouse_pos_hud
                self.cmpt = 2
        else:
            if  self.mouse_pos_hud[0]> self.first_pos[0]:
                for x in range( self.first_pos[0],  self.mouse_pos_hud[0] + 1):
                    if  self.mouse_pos_hud[1] > self.first_pos[1]:
                        for y in range( self.first_pos[1],  self.mouse_pos_hud[1] + 1):
                            hud_btn_controller.destruction(x,y)
                    else:
                        for y in range( self.mouse_pos_hud[1],  self.first_pos[1] + 1):
                            hud_btn_controller.destruction(x,y)
            else:
                for x in range( self.mouse_pos_hud[0], self.first_pos[0]+1):
                    if  self.mouse_pos_hud[1] >  self.first_pos[1]:
                        for y in range( self.first_pos[1], self.mouse_pos_hud[1]+1):
                            hud_btn_controller.destruction(x,y)
                    else:
                        for y in range ( self.mouse_pos_hud[1], self.first_pos[1]+1):
                            hud_btn_controller.destruction(x,y)
            self.mouse_pos_hud = (0,0)
            self.cmpt = 1
            self.first_pos = (0,0)

    def update(self):
        camera_controller = CameraController(self.game.camera)

        camera_controller.update()

    def draw(self):
        self.game.screen.fill((0, 0, 0))
        # level
        self.game.level.draw(self.game.screen, self.game.camera)
        # HUD
        self.game.level.hud.display_hud()

        hud_btn_controller = HUDButtonController(self.game.level.hud)
        road_btn = Button(pg.Rect(1268, 299, 42, 29), "", hud_btn_controller.create_road)
        road_btn.hover(self.game.screen, road_btn) 

        pg.display.flip()