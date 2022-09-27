import pygame as pg

class CameraController:
    def __init__(self, camera):
        self.camera = camera

    def update(self):
        mouse_pos = pg.mouse.get_pos()

        # x movement
        if mouse_pos[0] > self.camera.width * 0.97:
            self.dx = -self.camera.speed
        elif mouse_pos[0] < self.camera.width * 0.03:
            self.dx = self.camera.speed
        else:
            self.dx = 0

        # y movement
        if mouse_pos[1] > self.camera.height * 0.97:
            self.dy = -self.camera.speed
        elif mouse_pos[1] < self.camera.height * 0.03:
            self.dy = self.camera.speed
        else:
            self.dy = 0

        # update camera scroll
        self.camera.scroll.x += self.dx
        self.camera.scroll.y += self.dy