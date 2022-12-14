import pygame as pg
from pygame.locals import *
from controller.utils import *
from view.button import Button

class HUD():
    """A HUD."""

    def __init__(self, level):
        """HUD constructor.
        
        Argument:
            level -- game level
        """
        self.level = level


        self.buttons = []
        self.subbuttons = []

        self.fct = ""
        self.fctselected = False
        self.subfctselected = False
       
    def blit_right_panel(self):
        """Blit right panel HUD."""
        l_right_panel = load_right_panel()
   
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



   
    def blit_top_menu(self, money, workers, citizens, food):
        """Blit top menu HUD."""
        l_top_panel = load_top_menu()

        self.top_menu.blit(l_top_panel[1],(0,0))
        self.top_menu.blit(l_top_panel[9],(24,0))
        self.top_menu.blit(l_top_panel[3],(48,0))
        self.top_menu.blit(l_top_panel[4],(72,0))
        self.top_menu.blit(l_top_panel[5],(96,0))
        self.top_menu.blit(l_top_panel[6],(120,0))
        self.top_menu.blit(l_top_panel[7],(144,0))
        self.top_menu.blit(l_top_panel[8],(168,0))
        self.top_menu.blit(l_top_panel[2],(192,0))
        self.top_menu.blit(l_top_panel[10],(216,0))
        self.top_menu.blit(l_top_panel[3],(256,0))
        self.top_menu.blit(l_top_panel[4],(280,0))
        self.top_menu.blit(l_top_panel[5],(304,0))
        self.top_menu.blit(l_top_panel[6],(328,0))
        self.top_menu.blit(l_top_panel[7],(352,0))
        self.top_menu.blit(l_top_panel[8],(376,0))
        self.top_menu.blit(l_top_panel[2],(400,0))
        self.top_menu.blit(l_top_panel[10],(424,0))
        self.top_menu.blit(l_top_panel[3],(464,0))
        self.top_menu.blit(l_top_panel[4],(488,0))
        self.top_menu.blit(l_top_panel[5],(512,0))
        self.top_menu.blit(l_top_panel[6],(536,0))
        self.top_menu.blit(l_top_panel[7],(560,0))
        self.top_menu.blit(l_top_panel[8],(584,0))
        self.top_menu.blit(l_top_panel[2],(608,0))
        self.top_menu.blit(l_top_panel[10],(632,0))
        self.top_menu.blit(l_top_panel[0],(672,0))
        self.top_menu.blit(l_top_panel[8],(792,0))
        self.top_menu.blit(l_top_panel[12],(816,0))
        self.top_menu.blit(l_top_panel[3],(832,0))
        self.top_menu.blit(l_top_panel[4],(856,0))
        self.top_menu.blit(l_top_panel[5],(880,0))
        self.top_menu.blit(l_top_panel[6],(904,0))
        self.top_menu.blit(l_top_panel[0],(928,0))
        self.top_menu.blit(l_top_panel[7],(1048,0))
        self.top_menu.blit(l_top_panel[8],(1072,0))
        self.top_menu.blit(l_top_panel[2],(1096,0))
        self.top_menu.blit(l_top_panel[10],(1120,0))
        self.top_menu.blit(l_top_panel[0],(1160,0))
        self.top_menu.blit(l_top_panel[9],(1280,0))
        self.top_menu.blit(l_top_panel[11],(1304,0))
        self.top_menu.blit(l_top_panel[5],(1336,0))
        font = pg.font.Font("assets/font/Centurion-Regular.ttf", 20)
        image_text = font.render("Dinars   "+str(money), 1, (255, 255, 255))
        image_text2 = font.render("Citizens   "+str(citizens), 1, (255, 255, 255))
        image_text3 = font.render("Workers   "+str(workers), 1, (255, 255, 255))
        image_text4 = font.render("Food   "+str(food), 1, (255, 255, 255))
        self.top_menu.blit(image_text,(1098,3))
        self.top_menu.blit(image_text2,(600,3))
        self.top_menu.blit(image_text3,(848,3))
        self.top_menu.blit(image_text4,(300,3))

    def display_hud(self, window, money, workers, citizens, food):
        """Display the game HUD."""
        pg.init()

        self.fake_screen = pg.Surface((1360,765))
        self.right_panel = self.fake_screen.subsurface(1157, 24, 202, 735)
        self.top_menu = self.fake_screen.subsurface(0, 0, 1360, 24)

        self.blit_right_panel()
        self.blit_top_menu(money, workers, citizens, food)
        L, h = window.get_rect().size 
        self.buttons = []
        self.buttons.append(Button(pg.Rect(L*1168/1360, 302*h/765, 42*L/1360, 29*h/765), "create_house"))
        self.buttons.append(Button(pg.Rect(L*1218/1360, 302*h/765, 42*L/1360, 29*h/765), "destruction"))
        self.buttons.append(Button(pg.Rect(L*1268/1360, 302*h/765, 42*L/1360, 29*h/765), "create_road"))
        self.buttons.append(Button(pg.Rect(L*1168/1360, 338*h/765, 42*L/1360, 29*h/765), "waterworks"))
        self.buttons.append(Button(pg.Rect(L*1268/1360, 410*h/765, 42*L/1360, 29*h/765), "agriculture"))
        self.buttons.append(Button(pg.Rect(L*1168/1360, 410*h/765, 42*L/1360, 29*h/765), "engineerPost"))
        self.buttons.append(Button(pg.Rect(L*1168/1360, 449*h/765, 42*L/1360, 22*h/765), "unselected"))
      
        if(self.fct == "waterworks"):
            self.display_waterworkssubhud(window)

        if (self.fct == "agriculture"):
            self.display_agriculturesubhud(window)

        window.blit(pygame.transform.scale(self.top_menu,(L,h*24/765) ), (0, 0))
        window.blit(pygame.transform.scale(self.right_panel, (L*202/1360, h*740/765)), (L*1157/1360, h*24/765))

        for btn in self.buttons:
            btn.hover(window, btn, "HUD")

        pg.display.update()

    def display_waterworkssubhud(self, window):
        L, h = window.get_rect().size

        self.subbuttons = []
        self.subbuttons.append(Button(pg.Rect(L/2-300, 700, 500, 29), "Reservoir"))
        self.subbuttons.append(Button(pg.Rect(L/2-300, 736, 500, 29), "Aqueduct"))

        for btn in self.subbuttons:
            btn.hover(window, btn, "Sub Menu")

        

    def display_agriculturesubhud(self, window):
        L, h = window.get_rect().size

        self.subbuttons = []
        self.subbuttons.append(Button(pg.Rect(L/2-300, 700, 500, 29), "Granary"))
        self.subbuttons.append(Button(pg.Rect(L/2-300, 736, 500, 29), "Farm"))

        for btn in self.subbuttons:
            btn.hover(window, btn, "Sub Menu")

        