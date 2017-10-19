import pygame


class Tile(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("tile.png")

    def draw(self, surface):
        surface.blit(self.image, (self.x*20 + 100, self.y*20 + 100))

