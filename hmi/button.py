#! /usr/bin/env python3

import pygame

class Button():
    """A Button.
    
    Attributes:
        window: surface to display the button
        x: abscissa coordinate of the button
        y: ordinate coordinate of the button
        width: length of the button abscissa
        height: length of the button ordinate
        text: signification of the button
    """
    def __init__(self, window, x, y, width, height, text):
        """ Init a button with a window, a x, a y, 
        a width, a height and a text.
        """
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        """Draw a rectangle representing a button."""
        pygame.draw.rect(self.window, (220, 220, 220), pygame.Rect(self.x, self.y, self.width, self.height))