import sys
import pygame
from pygame.math import Vector2

from constants import cell_number, cell_size, background_color
from fruit import Fruit
from snake import Snake

pygame.init()
screen = pygame.display.set_mode(
    (cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

game_font = pygame.font.Font("fonts/PoetsenOne-Regular.ttf", 25)
apple = pygame.image.load("images/apple.png").convert_alpha()

snake = Snake()
fruit = Fruit()


def update():
    snake.move_snake()
    check_collision()
    check_fail()


def draw_elements():
    draw_grass()
    fruit.draw_fruit(screen)
    snake.draw_snake(screen)
    draw_score()


def check_collision():
    if fruit.pos == snake.body[0]:
        fruit.randomize()
        snake.add_block()
        snake.play_crunch_sound()

    for block in snake.body[1:]:
        if block == fruit.pos:
            fruit.randomize()


def check_fail():
    if not 0 <= snake.body[0].x < cell_number or not 0 <= snake.body[0].y < cell_number:
        game_over()

    for block in snake.body[1:]:
        if block == snake.body[0]:
            game_over()


def game_over():
    snake.reset()


def draw_grass():
    grass_color = (167, 209, 61)
    for row in range(cell_number):
        if row % 2 == 0:
            for col in range(cell_number):
                if col % 2 == 0:
                    grass_rect = pygame.Rect(
                        col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)
        else:
            for col in range(cell_number):
                if col % 2 != 0:
                    grass_rect = pygame.Rect(
                        col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)


def draw_score():
    score_text = str(len(snake.body) - 3)
    score_surface = game_font.render(score_text, True, (56, 74, 12))
    score_x = int(cell_size * cell_number - 60)
    score_y = int(cell_size * cell_number - 40)
    score_rect = score_surface.get_rect(center=(score_x, score_y))
    apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
    bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,
                          apple_rect.width + score_rect.width + 6, apple_rect.height)

    pygame.draw.rect(screen, (167, 209, 61), bg_rect)
    screen.blit(score_surface, score_rect)
    screen.blit(apple, apple_rect)
    pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake.direction.y != 1:
                    snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if snake.direction.x != -1:
                    snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if snake.direction.y != -1:
                    snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if snake.direction.x != 1:
                    snake.direction = Vector2(-1, 0)
    screen.fill(background_color)
    draw_elements()
    pygame.display.update()
    clock.tick(120)
