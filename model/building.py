import pygame as pg

class Building():
    
    def __init__(self, title, sprites, x_position, y_position, state, level):
        self.building_title = title
        self.building_sprites = sprites
        self.building_x = x_position
        self.building_y = y_position
        self.building_state = state
        self.building_level = level

    
