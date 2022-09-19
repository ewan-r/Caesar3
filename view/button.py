import pygame

class Button():
    """A Button.
        rect: rectangle of the button ordinate
        text: signification of the button
        ftn_click: function executed when the button is clicked
    """
    def __init__(self, rect, text, ftn_click):
        """ Init a button with a rectangle,
        a text and a function executed when a click is done.
        """
        self.rect = rect
        self.text = text
        self.ftn_click = ftn_click

    def draw(self, window, is_hovered):
        """Draw a rectangle representing a button."""

        if is_hovered == False:
            pygame.draw.rect(window, (149, 148, 116), self.rect, 0, 2, 2)

            font = pygame.font.Font("view/data/font/Forum-Regular.ttf", 25)
            text = font.render(self.text, 1, (0,0,0))
            # put the text at the center of the button
            window.blit(text, (self.rect.x + (self.rect.width/2 - text.get_width()/2), self.rect.y + (self.rect.height/2 - text.get_height()/2)))
        else:
            pygame.draw.rect(window, (0, 0, 0), self.rect, 2, 2)