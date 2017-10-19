import pygame
import math
class Ball(object):

    def __init__(self, x, y, max_x, max_y):
        self.x = x
        self.y = y
        self.max_x = max_x-1
        self.max_y = max_y-1
        self.direction = [-1,-1]
        self.ani_state = 0
        self.images = ["ball1.png", "ball2.png", "ball3.png", "ball4.png"]
        for i in range(4):
            self.images[i] = pygame.image.load(self.images[i])

    def move(self):
        if self.x + self.direction[0] < 0:
            self.direction[0] = 1
        if self.x + self.direction[0] > self.max_x:
            self.direction[0] = -1
        if self.y + self.direction[1] < 0:
            self.direction[1] = 1
        if self.y + self.direction[1] > self.max_y:
            self.direction[1] = -1
        self.x += self.direction[0]
        self.y += self.direction[1]

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def angle(self):
        return {(-1,-1): math.degrees((3*math.pi)/4), (-1,1): math.degrees((5*math.pi)/4),(1,-1): math.degrees(math.pi/4), (1,1): math.degrees((7*math.pi)/4)}[tuple(self.direction)]

    def draw(self, surface, progress=False):
        surface.blit(self.rot_center(self.images[self.ani_state],self.angle()), (self.x*20 + 100, self.y*20 + 100))
        if progress:
            self.move()
            self.ani_state += 1
            if self.ani_state >=4:
                self.ani_state = 0
