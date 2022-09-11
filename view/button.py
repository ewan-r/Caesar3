#! /usr/bin/env python3

import pygame

class Button():
    """A Button.
    
    Attributes:
        x: abscissa coordinate of the button
        y: ordinate coordinate of the button
        width: length of the button abscissa
        height: length of the button ordinate
        text: signification of the button
    """
    def __init__(self, x, y, width, height, text):
        """ Init a button a x, a y, a width, 
        a height and a text.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window):
        """Draw a rectangle representing a button."""
        pygame.draw.rect(window, (149, 148, 116), (self.x, self.y, self.width, self.height))

        font = pygame.font.Font("view/data/font/Forum-Regular.ttf", 25)
        text = font.render(self.text, 1, (0,0,0))
        # put the text at the center of the button
        window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))