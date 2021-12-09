from pygame.math import Vector2
from pygame.image import load
from pygame.mixer import Sound
from pygame import Rect, Surface

from constants import cell_size


class Snake():
    def __init__(self) -> None:
        self.body = self._get_default_body()
        self.direction = self._get_default_direction()
        self.new_block = False

        self.head_up = load("images/head_up.png").convert_alpha()
        self.head_down = load("images/head_down.png").convert_alpha()
        self.head_right = load("images/head_right.png").convert_alpha()
        self.head_left = load("images/head_left.png").convert_alpha()

        self.tail_up = load("images/tail_up.png").convert_alpha()
        self.tail_down = load("images/tail_down.png").convert_alpha()
        self.tail_right = load("images/tail_right.png").convert_alpha()
        self.tail_left = load("images/tail_left.png").convert_alpha()

        self.body_vertical = load("images/body_vertical.png").convert_alpha()
        self.body_vertical = load(
            'images/body_vertical.png').convert_alpha()

        self.body_tr = load('images/body_tr.png').convert_alpha()
        self.body_tl = load('images/body_tl.png').convert_alpha()
        self.body_br = load('images/body_br.png').convert_alpha()
        self.body_bl = load('images/body_bl.png').convert_alpha()
        self.crunch_sound = Sound('sounds/crunch.wav')

    def draw_snake(self, screen: Surface):
        self.update_head_graphics()
        self.update_tail_graphics()

        for idx, block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = Rect(x_pos, y_pos, cell_size, cell_size)

            if idx == 0:
                screen.blit(self.head, block_rect)
            elif idx == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                pass

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = self._get_default_body()
        self.direction = self._get_default_direction()

    def _get_default_body(self):
        return [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]

    def _get_default_direction(self):
        return Vector2(0, 0)
