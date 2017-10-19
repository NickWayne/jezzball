from tile import Tile
from ball import Ball
import random
class Field(object):

    def __init__(self, width, height, balls):
        self.width = width
        self.height = height
        self.board = [[]]
        self.balls = []
        for i in range(balls):
            self.balls.append(Ball(random.randint(1,self.width-1), random.randint(1,self.height-1), self.width, self.height))
        for i in range(height):
            for g in range(width):
                self.board[i].append(Tile(g,i))
            self.board.append([])

    def re_ball(self, number):
        self.balls = []
        for i in range(number):
            self.balls.append(Ball(random.randint(1, self.width - 1), random.randint(1, self.height - 1), self.width, self.height))
    def draw(self, surface, balls=False):
        for i in self.board:
            for g in i:
                g.draw(surface)
        for i in self.balls:
            if balls:
                i.draw(surface, True)
            else:
                i.draw(surface)
