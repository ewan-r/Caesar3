import pygame as pg

class Camera:
    """A Camera."""

    def __init__(self, width, height):
        """Camera constructor.
        
        Arguments:
            width -- grid width
            height -- grid height
        """
        self.width = width
        self.height = height

        self.scroll = pg.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.speed = 25