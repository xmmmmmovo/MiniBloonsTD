import sys
import pygame
import pygame.freetype

pygame.init()

v_info = pygame.display.Info()
size = width, height = 600, 400
speed = [1, 1]
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

still = False

bgcolor = pygame.Color("black")

def RGBChannel(a):
    return 0 if a < 0 else (255 if a > 5 else int(a))


while True:
    # uevent = pygame.event.Event(
    # pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_SPACE, "mod": pygame.KMOD_ALT})
    # pygame.event.post(uevent)

    for event in pygame.event.get():
        # 处理事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("#", event.key, event.mod)
            else:
                print(event.unicode, event.key, event.mod)

            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (
                    abs(speed[0]) - 1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (
                    abs(speed[1]) - 1)*int(speed[1]/abs(speed[1]))
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEMOTION:
            print("mouse motion", event.pos, event.rel, event.buttons)
            if event.buttons[0] == 1:
                ballrect = ballrect.move(
                    event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("mouse up", event.pos,  event.button)
            still = False
            if event.button == 1:
                ballrect = ballrect.move(
                    event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse down", event.pos, event.button)
            if event.button == 1:
                still = True

    # 判断是否最小化了
    if pygame.display.get_active() and not still:
        ballrect = ballrect.move(speed)

    # print(speed[0], ":", speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
        if ballrect.left > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = -speed[1]

    bgcolor.r = RGBChannel(ballrect.left * 255 / width)
    bgcolor.g = RGBChannel(ballrect.top * 255 / height)
    bgcolor.b = RGBChannel(
        min(speed[0], speed[1]) * 255 / max(speed[0], speed[1], 1))

    screen.fill(bgcolor)
    screen.blit(ball, ballrect)
    pygame.display.update()
    fclock.tick(fps)
