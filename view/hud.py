#Imports
import pygame
from pygame.locals import * 
from image_import import *
from button import Button

class HUD():
    """
    Display the top menu and right panel of the HUD
    """

    def __init__(self, window, state):
        """Init HUD"""
        self.window = window
        self.state = state
        self.right_panel = window.subsurface(1157, 24, 202, 735)
        self.top_menu = window.subsurface(0, 0, 1360, 24)
        self.state = state
       
    def blit_right_panel(self):
#TO DO : tableau avec coordonnées, à blit dans cette fonction
# self.right_panel
   
        self.right_panel.blit(gui_background1,(0,0))
        self.right_panel.blit(gui_background2,(0,450))

        #4,5
        self.right_panel.blit(right_panel_arrow,(127,5))
        #4,3
        self.right_panel.blit(overlays_back,(4,3))
        #7,155
        self.right_panel.blit(right_panel_guys,(7,155))
        #7,84
        self.right_panel.blit(right_panel_map,(84,155))
        #7,184
        self.right_panel.blit(quest_icon,(7,(184)))
        #46, 184
        self.right_panel.blit(north_icon,((46),(184)))
        #84, 184
        self.right_panel.blit(Larrow_icon,((84),(184)))
        #123, 184
        self.right_panel.blit(Rarrow_icon,((123),(184)))
        #7, 216 
        self.right_panel.blit(right_panel_deco,((7),(216)))
        #13, 277
        self.right_panel.blit(home_icon,((13),(277)))
        #63, 277
        self.right_panel.blit(shovel_icon,((63),(277)))
        #113, 277
        self.right_panel.blit(pass_icon,((113),(277)))
        #13, 313
        self.right_panel.blit(water_icon,((13),(313)))
        #63, 313
        self.right_panel.blit(plus_icon,((63),(313)))
        #113, 313
        self.right_panel.blit(flash_icon,((113),(313)))
        #13, 349
        self.right_panel.blit(parchment_icon,((13),(349)))
        #63, 349
        self.right_panel.blit(mask_icon,((63),(349)))
        #113, 349
        self.right_panel.blit(temple_icon,((113),(349)))
        #13, 385
        self.right_panel.blit(hammer_icon,((13),(385)))
        #63, 385
        self.right_panel.blit(sword_icon,((63),(385)))
        #113, 385
        self.right_panel.blit(farm_icon,((113),(385)))
        #13, 421
        self.right_panel.blit(cross_icon,((13),(421)))
        #63, 421
        self.right_panel.blit(sign_icon,((63),(421)))
        #113, 421
        self.right_panel.blit(bell_icon,((113),(421)))
        #right band motiv
        for i in range (0,30):
            self.right_panel.blit(lat_bar, (162,24*i))
        self.right_panel.blit(lat_bar, (162,711))

   
    def blit_top_menu(self):
        self.top_menu.blit(top_menu1,(0,0))
        self.top_menu.blit(top_menu9,(24,0))
        self.top_menu.blit(top_menu3,(48,0))
        self.top_menu.blit(top_menu4,(72,0))
        self.top_menu.blit(top_menu5,(96,0))
        self.top_menu.blit(top_menu6,(120,0))
        self.top_menu.blit(top_menu7,(144,0))
        self.top_menu.blit(top_menu8,(168,0))
        self.top_menu.blit(top_menu2,(192,0))
        self.top_menu.blit(top_menu10,(216,0))
        self.top_menu.blit(top_menu3,(256,0))
        self.top_menu.blit(top_menu4,(280,0))
        self.top_menu.blit(top_menu5,(304,0))
        self.top_menu.blit(top_menu6,(328,0))
        self.top_menu.blit(top_menu7,(352,0))
        self.top_menu.blit(top_menu8,(376,0))
        self.top_menu.blit(top_menu2,(400,0))
        self.top_menu.blit(top_menu10,(424,0))
        self.top_menu.blit(top_menu3,(464,0))
        self.top_menu.blit(top_menu4,(488,0))
        self.top_menu.blit(top_menu5,(512,0))
        self.top_menu.blit(top_menu6,(536,0))
        self.top_menu.blit(top_menu7,(560,0))
        self.top_menu.blit(top_menu8,(584,0))
        self.top_menu.blit(top_menu2,(608,0))
        self.top_menu.blit(top_menu10,(632,0))
        self.top_menu.blit(bubble_menu,(672,0))
        self.top_menu.blit(top_menu8,(792,0))
        self.top_menu.blit(bubble_menu,(816,0))
        self.top_menu.blit(top_menu12,(936,0))
        self.top_menu.blit(top_menu3,(952,0))
        self.top_menu.blit(top_menu4,(976,0))
        self.top_menu.blit(top_menu5,(1000,0))
        self.top_menu.blit(top_menu6,(1024,0))
        self.top_menu.blit(top_menu7,(1048,0))
        self.top_menu.blit(top_menu8,(1072,0))
        self.top_menu.blit(top_menu2,(1096,0))
        self.top_menu.blit(top_menu10,(1120,0))
        self.top_menu.blit(bubble_menu,(1160,0))
        self.top_menu.blit(top_menu9,(1280,0))
        self.top_menu.blit(top_menu11,(1304,0))
        self.top_menu.blit(top_menu5,(1336,0))


    def display_HUD(self):
        """Display HUD"""
        #Initialise screen
        pygame.init()
        pygame.display.set_caption("INSAlubrity III ")
        self.blit_right_panel()
        self.blit_top_menu()
        pygame.display.update()

        #Event loop
        disp = 1

        while disp:
            event = pygame.event.wait()

            if event.type == QUIT:
                disp = 0

                pygame.display.update()
                pygame.display.flip()

