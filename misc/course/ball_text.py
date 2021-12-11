import os
import sys
import pygame
import pygame.freetype

pygame.init()

v_info = pygame.display.Info()
size = width, height = 600, 400
speed = [1, 1]
pos = [230, 160]
screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # 窗口大小可调
# screen = pygame.display.set_mode(size, pygame.NOFRAME)  #窗口无边框
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)  #窗口全屏显示

pygame.display.set_caption("Pygame壁球")
icon = pygame.image.load("PYG03-flower.png")
pygame.display.set_icon(icon)
ball = pygame.image.load("PYG02-ball.gif")
ballrect = ball.get_rect()

fps = 300
fclock = pygame.time.Clock()

bgcolor = pygame.Color("black")
GOLD = 255, 251, 0

# print(pygame.font.get_fonts())
f1 = pygame.freetype.SysFont("applesdgothicneo", 36)
f1rect = f1.render_to(screen, pos, "世界和平", fgcolor=GOLD, size=50)

while True:
    # uevent = pygame.event.Event(
    # pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_SPACE, "mod": pygame.KMOD_ALT})
    # pygame.event.post(uevent)

    for event in pygame.event.get():
        # 处理事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if pos[0] < 0 or pos[0] + f1rect.width > width:
        speed[0] = -speed[0]
    if pos[1] < 0 or pos[1] + f1rect.height > height:
        speed[1] = -speed[1]

    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]

    screen.fill(bgcolor)
    f1rect = f1.render_to(screen, pos, "世界和平", fgcolor=GOLD, size=50)
    pygame.display.update()
    fclock.tick(fps)
