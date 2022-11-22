from cmath import rect
import pygame as pg
import sys
import time

from model.storage import Storage
from controller.camera_controller import CameraController
from view.pause_menu import PauseMenu

class GameController:
    def __init__(self, game):
        pg.init()
        self.BTN_W = 400
        self.BTN_H = 40 
       
        
        self.game = game
        self.playing = False
        self.screen = self.game.screen
        self.width, self.height = pg.display.get_surface().get_size()
        self.menuNew = PauseMenu(self.screen, "")
        
        """self.save_game_button = GameButton("Save game", self.screen, (200,200), 20, feedback="game saved!")
        self.load_game_button = GameButton("Load game", self.screen, (200,220), 20, feedback="game saved!")
        self.exit_game_button = GameButton("Continue", self.screen, (200,240), 20, feedback="game saved!")
        self.continue_game_button = GameButton("Exit to main menu", self.screen, (200,260), 20, feedback="game saved!")
       """
       
    def run(self):
        self.playing = True
        while self.playing:
            self.game.clock.tick(60)
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    
                    self.playing = False
                    '''
                    Show the menu
                    '''

                    commandResp = self.menuNew.display_menu()
                    command = commandResp[0]
                    if (command == "Exit to Main Menu"):
                        pg.quit
                        sys.exit()
                    elif(command == "Continue"):
                        pass
                    elif(command == "Save game"):
                        commandResp2 = self.menuNew.save()
                        command = commandResp2[0]
                        destination_file = commandResp2[1]
                        # if save Game option is selected from Pause Menu
                        if(command == "Cancel"):
                            pass
                        elif(command == "Save"):
                            self.save_game(destination_file)

                    self.playing = True

                if event.key == pg.K_2:
                    pg.quit()
                    sys.exit()

    def update(self):
        camera_controller = CameraController(self.game.camera)
        
        camera_controller.update()

    def draw(self):
        self.game.screen.fill((0, 0, 0))
        self.game.level.draw(self.game.screen, self.game.camera)

        pg.display.flip()

    def button(self, screen, position, text):
        font = pg.font.SysFont("Times New Roman", 40)
        text_render = font.render(text, 1, (0, 0, 0))
        x, y, w , h = text_render.get_rect()
        x, y = position
        #pg.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
        #pg.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        #pg.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        #pg.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
        pg.draw.rect(screen, (110, 110, 110), (x, y, self.BTN_W , self.BTN_H))
        return screen.blit(text_render, (x - (x - 3 * w)/6, y))

    """ Save the game state """
    def save_game(self, filename):
        gameData = Storage(self.game.level.level)
        gameData.save_game(filename + ".txt")
    
    def show_save_menu(self, window):
        print("test 1 2 3")
        pg.draw.rect(window, (255, 0, 0), (self.width/4, self.height/4, self.width/4 , self.height/4))
        pg.display.flip()
        time.sleep(200)

    def menu(self):
        
        """ This is the menu that waits you to click the s key to start """
        HEIGHT_EDGE = 50
        pg.draw.rect(self.screen, (100, 100, 100), (self.width/3, self.height/3, self.width/3 , self.height/3))
        save_button = self.button(self.screen, (self.width/3, self.height/3), "Save Game")
        load_button = self.button(self.screen, (self.width/3, self.height/3 + HEIGHT_EDGE), "Load Game")
        exit_button = self.button(self.screen, (self.width/3, self.height/3 + 2*HEIGHT_EDGE), "Exit Game")
        
        pg.display.update()

        while True:
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    pg.quit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if save_button.collidepoint(pg.mouse.get_pos()):
                        #self.save_game()
                        pg.init()
                        window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
                        return self.show_save_menu(window)
                        
                    elif exit_button.collidepoint(pg.mouse.get_pos()):
                        pg.quit()
                        return
        pg.quit()

   