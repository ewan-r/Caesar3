import pygame as pg

class NewButton():
    """A Button."""
    
    def __init__(self, rect, text, window):
        """Button constructor.

        Arguments:
            rect -- rectangle of the button ordinate
            text -- signification of the button
            ftn_click -- function executed when the button is clicked
        """
        self.rect = rect
        self.text = text
        self.window = window

    def getCommand(self):
        return self.text

    def draw(self, window, is_hovered):
        """Draw a rectangle representing a button.
        
        Arguments:
            window -- surface to display infomations
            is_hovered -- True if the button is hovered, False if it isn't
        """

        if is_hovered == False:
            pg.draw.rect(window, (149, 148, 116), self.rect, 0, 2, 2)

            font = pg.font.Font("assets/font/Forum-Regular.ttf", 25)
            text = font.render(self.text, 1, (0,0,0))
            # put the text at the center of the button
            window.blit(text, (self.rect.x + (self.rect.width/2 - text.get_width()/2), self.rect.y + (self.rect.height/2 - text.get_height()/2)))
        else:            
            pg.draw.rect(window, (0, 0, 0), self.rect, 2, 2)


    def hover(self, btn):
        """Modify the border radius of a button when the mouse hover it.
        
        Argument:
            btn -- button on which the border radius is changed
        """
        is_hovered = False

        if btn.rect.collidepoint(pg.mouse.get_pos()):
            is_hovered = True
            btn.draw(self.window, is_hovered)
        else:
            btn.draw(self.window, is_hovered)