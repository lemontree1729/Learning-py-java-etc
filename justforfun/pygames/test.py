import sys
from random import randint

from pgtools import *

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
ball = Ball(10, spd=(10, 10))
balls.add(ball)
cnt = 10
radius = 10
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    balls.update()
    screen.fill(BLACK)
    ball.draw(screen)
    cnt -= 1
    if cnt < 0:
        radius = (radius + 2) % 10
        ball.changeRadius(10 + radius)
        cnt = 10
    print(a)
    pg.display.update()
    fpscheck.tick(FPS)
