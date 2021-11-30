import sys
from random import randint
from collections import deque
from movingobject import *

# make error if pygame is not installed
try:
    import pygame as pg
except ModuleNotFoundError:
    print("ModuleError: you should install pg")
    sys.exit(1)


FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MINT = (0, 255, 255)
YELLOW = (255, 255, 0)
MAX_WIDTH, MAX_HEIGHT = 600, 400
score_left, score_right = 0, 0

pg.init()
fpscheck = pg.time.Clock()
screen = pg.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
pg.display.set_caption("Test")
balls = pg.sprite.Group()
balls.add(Ball(10, spd=(10, 10)))
bat = Bat((100, 15), cord=(300, 375))
bottomLine = BorderLine(direction="horizontal", pos=MAX_HEIGHT - 1)
cnt = 10
ball1 = Ball(10, spd=(-10, 10))
centers = deque([])
while 1:
    v1 = pg.math.Vector2(1, -2)
    v2 = pg.math.Vector2(1, 0)
    v3 = v1.reflect(v2)
    print(v1, v2, v3)
    print(v2 - v1)
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pressed_keys = pg.key.get_pressed()
    for center in centers:
        pg.draw.circle(screen, randomBrightRGB(), center, 2)
    centers.append(ball1.rect.center)
    if len(centers) > 15:
        centers.popleft()
    ball1.update()
    ball1.draw(screen)
    if pressed_keys[pg.K_LEFT]:
        bat.moveOnce((-20, 0))
    if pressed_keys[pg.K_RIGHT]:
        bat.moveOnce((20, 0))
    bottomLine.xyGroupCollide(balls, kill=True)
    for ball in balls:
        ball.xyCollide(bat, x=False)
    balls.update()
    bat.update()
    cnt -= 1
    if cnt < 0:
        balls.add(Ball(10, spd=(10, 10)))
        print(balls)
        for ball in balls:
            ball.changeRadius(10 + (ball.radius + 2) % 10)
        cnt = 10
    bottomLine.draw(screen)
    balls.draw(screen)
    bat.draw(screen)
    pg.display.update()
    fpscheck.tick(FPS)
