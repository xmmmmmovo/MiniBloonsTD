import pygame

from random import randint

from pygame.math import Vector2
from pygame.draw import rect

from constants import cell_number, cell_size, fruit_color


class Fruit:
    def __init__(self) -> None:
        self.x = randint(0, cell_number - 1)
        self.y = randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self, screen):
        fruit_rect = pygame.Rect(
            self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        rect(screen, fruit_color, fruit_rect)
