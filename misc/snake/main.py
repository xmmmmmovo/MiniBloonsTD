import sys
import pygame

from constants import cell_number, cell_size, background_color
from fruit import Fruit

pygame.init()
screen = pygame.display.set_mode(
    (cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

fruit = Fruit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(background_color)
    fruit.draw_fruit(screen)
    pygame.display.update()
    clock.tick(60)
