import pygame
import sys
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("文字绘制")
GOLD = 255, 251, 0

# print(pygame.font.get_fonts())
f1 = pygame.freetype.SysFont("applesdgothicneo", 36)
# f1rect = f1.render_to(screen, (200, 160), "世界和平", fgcolor=GOLD, size=50)

f1surf, f1rect2 = f1.render("世界和平", fgcolor=GOLD, size=50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(f1surf, (200, 160))
    pygame.display.update()
