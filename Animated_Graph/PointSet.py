import pygame
from SETTINGS import *


class Point(pygame.sprite.Sprite):
    def __init__(self, pos: list | tuple, index: int) -> None:
        super().__init__()
        self.pos: list = list(pos)
        self.index = index

        self.originalX = self.pos[0]
        self.originalY = self.pos[1]

        self.graph_x = WIDTH//2 + self.pos[0]
        self.graph_y = HEIGHT//2 - self.pos[1]

    def change_pos(self, pos: list | tuple) -> None:
        self.pos = list(pos)

    def draw(self, window: pygame.Surface):
        self.graph_x = WIDTH//2 + self.pos[0]
        self.graph_y = HEIGHT//2 - self.pos[1]

        pygame.draw.circle(window, "green", self.pos, 2)


class PointGroup:
    def __init__(self) -> None:
        self.PointGroup: list = []

    def assign(self, point: Point):
        self.PointGroup.append(point)

    def give(self) -> list:
        return self.PointGroup


def makePosition(x, y):
    return [WIDTH//2 + x, HEIGHT//2 - y]

# Checks if a point is out of bounds.
def OSP(pointgroup: PointGroup) -> int:
    i = 0
    for points in pointgroup.give():
        if 0 < points.pos[0] < 800:
            i += 1
    return i
