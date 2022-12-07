import pygame as pg
import glob

class TextField:
    def __init__(self, option,window, left, top, width, height):
        self.window = window
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.font = pg.font.Font(None, 32) # default font-size 32
        self.font_list = pg.font.Font(None, 25)
        self.input_field = pg.Rect(left, top, width, height) #100, 100, 140,32
        self.color = self.color_inactive
        self.text = ''
        self.option = option

    def setFont(self, size):
        self.font = pg.font.Font(None, size)

    def setActiveColor(self, color):
        self.color_active = pg.Color(color)

    def setInactiveColor(self, color):
         self.color_inactive = pg.Color(color)

    def render_window(self, buttons_save):
        
        active = True
        
        done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for btn in buttons_save:
                            if btn.rect.collidepoint(event.pos):
                            # return a string corresponding to the command 
                               btn.appendMessage(self.text)
                               return btn.getCommand() 

                    # If the user clicked on the input_box rect.
                    if self.input_field.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    self.color = self.color_active if active else self.color_inactive
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return
                    
                    if active:
                        if event.key == pg.K_RETURN:
                            print(self.text)
                            self.text = ''
                
                        elif event.key == pg.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
                    
            pg.draw.rect(self.window, (100, 100, 100), (self.window.get_size()[0]/2-155, 120, 310, 325))
            
            # Render the current text.
            txt_surface = self.font.render(self.text, True, self.color)
            
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            self.input_field.w = width
            
            # Blit the text.
            self.window.blit(txt_surface, (self.input_field.x+5, self.input_field.y+5))
            
            if(self.option == "load"):
                self.retrieve_filename()
            # Blit the input_box rect.
            pg.draw.rect(self.window, self.color, self.input_field, 2)

             # activate hover effect
            for btn in buttons_save:
                btn.hover(btn)
                
            pg.display.flip()

    def retrieve_filename(self):
        # read folder for saved files
        mylist = [f for f in glob.glob("model/storage/*.bin")]
    
        pos = 50

        if len(mylist) > 2:
            for i in range (len(mylist)-4,len(mylist),1):
                txt_surface = self.font_list.render(mylist[i][14:-4], True, self.color)
                self.window.blit(txt_surface, (self.input_field.x+5, self.input_field.y+pos))
                pos+=20