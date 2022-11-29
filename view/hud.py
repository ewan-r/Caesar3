import pygame as pg
from pygame.locals import * 
from controller.utils import *

class HUD():
    """
    Display the top menu and right panel of the HUD
    """
    def __init__(self, level):
        """Init HUD"""
        self.level = level

        window = pg.display.set_mode((1360, 765))

        self.right_panel = window.subsurface(1157, 24, 202, 735)
        self.top_menu = window.subsurface(0, 0, 1360, 24)
       
    def blit_right_panel(self):
        l_right_panel = load_right_panel()

        # TO DO : tableau avec coordonnées, à blit dans cette fonction
        # self.right_panel
   
        self.right_panel.blit(l_right_panel[0],(0,0))
        self.right_panel.blit(l_right_panel[1],(0,450))

        #4,5
        self.right_panel.blit(l_right_panel[2],(127,5))
        #4,3
        self.right_panel.blit(l_right_panel[3],(4,3))
        #7,155
        self.right_panel.blit(l_right_panel[4],(7,155))
        #7,84
        self.right_panel.blit(l_right_panel[5],(84,155))
        #7,184
        self.right_panel.blit(l_right_panel[6],(7,(184)))
        #46, 184
        self.right_panel.blit(l_right_panel[7],((46),(184)))
        #84, 184
        self.right_panel.blit(l_right_panel[8],((84),(184)))
        #123, 184
        self.right_panel.blit(l_right_panel[9],((123),(184)))
        #7, 216 
        self.right_panel.blit(l_right_panel[10],((7),(216)))
        #13, 277
        self.right_panel.blit(l_right_panel[11],((13),(277)))
        #63, 277
        self.right_panel.blit(l_right_panel[12],((63),(277)))
        #113, 277
        self.right_panel.blit(l_right_panel[13],((113),(277)))
        #13, 313
        self.right_panel.blit(l_right_panel[14],((13),(313)))
        #63, 313
        self.right_panel.blit(l_right_panel[15],((63),(313)))
        #113, 313
        self.right_panel.blit(l_right_panel[16],((113),(313)))
        #13, 349
        self.right_panel.blit(l_right_panel[17],((13),(349)))
        #63, 349
        self.right_panel.blit(l_right_panel[18],((63),(349)))
        #113, 349
        self.right_panel.blit(l_right_panel[19],((113),(349)))
        #13, 385
        self.right_panel.blit(l_right_panel[20],((13),(385)))
        #63, 385
        self.right_panel.blit(l_right_panel[21],((63),(385)))
        #113, 385
        self.right_panel.blit(l_right_panel[22],((113),(385)))
        #13, 421
        self.right_panel.blit(l_right_panel[23],((13),(421)))
        #63, 421
        self.right_panel.blit(l_right_panel[24],((63),(421)))
        #113, 421
        self.right_panel.blit(l_right_panel[25],((113),(421)))

        #right band motiv
        for i in range (0,30):
            self.right_panel.blit(l_right_panel[26], (162,24*i))
        self.right_panel.blit(l_right_panel[26], (162,711))

   
    def blit_top_menu(self):
        l_top_panel = load_top_menu()

        self.top_menu.blit(l_top_panel[0],(0,0))
        self.top_menu.blit(l_top_panel[1],(24,0))
        self.top_menu.blit(l_top_panel[2],(48,0))
        self.top_menu.blit(l_top_panel[3],(72,0))
        self.top_menu.blit(l_top_panel[4],(96,0))
        self.top_menu.blit(l_top_panel[5],(120,0))
        self.top_menu.blit(l_top_panel[6],(144,0))
        self.top_menu.blit(l_top_panel[7],(168,0))
        self.top_menu.blit(l_top_panel[8],(192,0))
        self.top_menu.blit(l_top_panel[9],(216,0))
        self.top_menu.blit(l_top_panel[10],(256,0))
        self.top_menu.blit(l_top_panel[11],(280,0))
        self.top_menu.blit(l_top_panel[12],(304,0))
        self.top_menu.blit(l_top_panel[13],(328,0))
        self.top_menu.blit(l_top_panel[14],(352,0))
        self.top_menu.blit(l_top_panel[15],(376,0))
        self.top_menu.blit(l_top_panel[16],(400,0))
        self.top_menu.blit(l_top_panel[17],(424,0))
        self.top_menu.blit(l_top_panel[18],(464,0))
        self.top_menu.blit(l_top_panel[19],(488,0))
        self.top_menu.blit(l_top_panel[20],(512,0))
        self.top_menu.blit(l_top_panel[21],(536,0))
        self.top_menu.blit(l_top_panel[22],(560,0))
        self.top_menu.blit(l_top_panel[23],(584,0))
        self.top_menu.blit(l_top_panel[24],(608,0))
        self.top_menu.blit(l_top_panel[25],(632,0))
        self.top_menu.blit(l_top_panel[26],(672,0))
        self.top_menu.blit(l_top_panel[27],(792,0))
        self.top_menu.blit(l_top_panel[28],(816,0))
        self.top_menu.blit(l_top_panel[29],(936,0))
        self.top_menu.blit(l_top_panel[30],(952,0))
        self.top_menu.blit(l_top_panel[31],(976,0))
        self.top_menu.blit(l_top_panel[32],(1000,0))
        self.top_menu.blit(l_top_panel[33],(1024,0))
        self.top_menu.blit(l_top_panel[34],(1048,0))
        self.top_menu.blit(l_top_panel[35],(1072,0))
        self.top_menu.blit(l_top_panel[36],(1096,0))
        self.top_menu.blit(l_top_panel[37],(1120,0))
        self.top_menu.blit(l_top_panel[38],(1160,0))
        self.top_menu.blit(l_top_panel[39],(1280,0))
        self.top_menu.blit(l_top_panel[40],(1304,0))
        self.top_menu.blit(l_top_panel[41],(1336,0))

    def display_hud(self):
        """Display HUD"""
        self.blit_right_panel()
        self.blit_top_menu()