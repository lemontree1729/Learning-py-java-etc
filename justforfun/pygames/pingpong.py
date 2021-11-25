# pyinstaller --noconsole --onefile pingpong.py

import sys
from random import randint
from pgtools import *

# make error if pygame is not installed
try:
    import pygame as pg
except ModuleNotFoundError:
    print("ModuleError: you should install pg")
    sys.exit(1)

# initialize pygame
pg.init()

# global constant
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MINT = (0, 255, 255)
YELLOW = (255, 255, 0)
MAX_WIDTH, MAX_HEIGHT = 600, 400

# make timer and main screen
fpscheck = pg.time.Clock()
screen = pg.display.set_mode((MAX_WIDTH, MAX_HEIGHT))  # main surface
pg.display.set_caption("PingPong Game")

# text score
score_left, score_right = 0, 0
font = pg.font.SysFont("Ink Free", 50)
text_left = font.render(str(score_left), True, GREEN, BLUE)
text_right = font.render(str(score_right), True, GREEN, BLUE)
text_leftRect = text_left.get_rect()
text_leftRect.left, text_leftRect.top = 1, 1
text_rightRect = text_right.get_rect()
text_rightRect.right, text_rightRect.top = MAX_WIDTH - 1, 1

# ball group
balls = pg.sprite.Group()

# bat group
bats = pg.sprite.Group()
bat_R = Bat(screen, 10, 100, 575, MAX_HEIGHT / 2, YELLOW)
bat_L = Bat(screen, 10, 100, 25, MAX_HEIGHT / 2, MINT)  # 15, 100, 20, 150, MINT
bat_L.up, bat_L.down = pg.K_w, pg.K_s
bats.add(bat_L, bat_R)

# endline group
endLines = pg.sprite.Group()
leftEnd = EndLine(screen, "vertical", 0)
rightEnd = EndLine(screen, "vertical", MAX_WIDTH - 1)
topEnd = EndLine(screen, "horizontal", 0)
bottomEnd = EndLine(screen, "horizontal", MAX_HEIGHT - 1)
endLines.add(leftEnd, rightEnd, topEnd, bottomEnd)

# global variable
game_run = False

while 1:
    for event in pg.event.get():
        # press exit to exit
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    # press space to restart
    if pg.key.get_pressed()[pg.K_SPACE]:
        score_left, score_right = 0, 0
        game_run = True
        fpstick = 0
        balls = pg.sprite.Group()
    if game_run:
        if score_left >= 5 or score_right >= 5:
            if score_left > score_right:
                score_left, score_right = "W", "L"
            else:
                score_left, score_right = "L", "W"
            game_run = False  # stop game until restart
        fpstick -= 1
        if fpstick < 0:
            vx, vy = (2 * randint(0, 1) - 1) * randint(10, 15), randint(0, 10)
            balls.add(Ball(screen, 10, 300, 200, vx, vy))
            fpstick = 30  # add balls for every 30 fps ticks
        for ball in balls:  # select ball
            ball.collided = False
            balls.remove(ball)
            checkLine = ball.checkCollide(endLines, x=False) or []
            # check collide with 4 edge lines
            if leftEnd in checkLine:
                print("left")
                score_left += 1
            elif rightEnd in checkLine:
                print("right")
                score_right += 1
            else:
                ball.checkCollide(bats, y=False)
                ball.checkCollide(endLines, x=False)
                for otherball in balls:
                    ball.ellasticCollide(otherball)  # ellastic collide
                balls.add(ball)
                ball.update()
    # bat update should be here because it should move whether game stops or not!
    bats.update()

    # drawing part
    screen.fill(BLACK)
    endLines.draw(screen)
    balls.draw(screen)
    bats.draw(screen)
    pg.draw.line(screen, GREEN, (MAX_WIDTH / 2, 0), (MAX_WIDTH / 2, MAX_HEIGHT))
    text_left = font.render(str(score_left), True, GREEN, BLUE)
    text_right = font.render(str(score_right), True, GREEN, BLUE)
    screen.blit(text_left, text_leftRect)
    screen.blit(text_right, text_rightRect)

    # finally update display and wait for tick
    pg.display.update()
    fpscheck.tick(FPS)
