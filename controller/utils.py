import pygame

def load_right_panel():
    #TO DO : Changer chemin, mettre laod dans même ordre que blit et import dans hud
    l_right_panel = []
    
    #162*450 : Gui background 1
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00017.png").convert_alpha())
    #162*120 : Gui background 2
    l_right_panel.append(pygame.image.load("assets/sprites/hud/map_panels_00003.png").convert_alpha())
    #31*20
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00097.png").convert_alpha())
    #117*25
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00234.png").convert_alpha())
    #71*23
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00079.png").convert_alpha())
    #71*23
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00082.png").convert_alpha())
    #33*22
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00085.png").convert_alpha())
    #33*22
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00088.png").convert_alpha())
    #33*22
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00091.png").convert_alpha())
    #33*22
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00094.png").convert_alpha())
    #149*54
    l_right_panel.append(pygame.image.load("assets/sprites/hud/panelwindows_00013.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00123.png").convert_alpha())
    #39*26 road
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00131.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00135.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00127.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00163.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00151.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00147.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00143.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00139.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00167.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00159.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00155.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00171.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00115.png").convert_alpha())
    #39*26
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00119.png").convert_alpha())
    #40*right_panel_h 
    l_right_panel.append(pygame.image.load("assets/sprites/hud/paneling_00013.png").convert_alpha())

    return l_right_panel

def load_top_menu():
    l_top_menu = []
    
    #120*24 : bubble menu
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00015.png").convert_alpha())
    #24*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00001.png").convert_alpha())
    #24*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00002.png").convert_alpha())
    #24*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00003.png").convert_alpha())
    #24*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00004.png").convert_alpha())
    #24*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00005.png").convert_alpha())
    #24*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00006.png").convert_alpha())
    #24*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00007.png").convert_alpha())
    #24*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00008.png").convert_alpha())
    #24*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00009.png").convert_alpha())

    #40*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00010.png").convert_alpha())
    #32*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00011.png").convert_alpha())
    #16*24
    l_top_menu.append(pygame.image.load("assets/sprites/hud/paneling_00012.png").convert_alpha())
    
    return l_top_menu