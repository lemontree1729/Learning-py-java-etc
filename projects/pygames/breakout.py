import sys
from random import randint
from pgtools import *
from time import time

try:
    import pygame as pg
except ModuleNotFoundError:
    print("ModuleError: you should install pg")
    sys.exit(1)

# global constants
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MINT = (0, 255, 255)
YELLOW = (255, 255, 0)
MAX_WIDTH, MAX_HEIGHT = 600, 400

# init
pg.init()
fpscheck = pg.time.Clock()
screen = pg.display.set_mode((MAX_WIDTH, MAX_HEIGHT))  # main surface
pg.display.set_caption("Breakout Game")

# bat group
bat_B = Bat(screen, 100, 15, MAX_WIDTH / 2, MAX_HEIGHT - 30, MINT)
bat_B.k_up, bat_B.k_down = None, None
bats = pg.sprite.Group()
bats.add(bat_B)

# brick group
def makeBricks(n, m, color=None):
    bricks = pg.sprite.Group()
    for y in range(n):
        for x in range(m):
            brick = Bat(screen, MAX_WIDTH / (m + 1) - 20, 15, MAX_WIDTH * (x + 1) / (m + 1), 50 * (y + 1), color)
            bricks.add(brick)
    return bricks


# ball group
balls = pg.sprite.Group()
ball = Ball(screen, 10, MAX_WIDTH / 2, MAX_HEIGHT / 2, randint(-10, 10), -10, RED)
balls.add(ball)

# endline group
verLines = pg.sprite.Group()
horLines = pg.sprite.Group()
leftEnd = EndLine(screen, "vertical", 0)
rightEnd = EndLine(screen, "vertical", MAX_WIDTH - 1)
topEnd = EndLine(screen, "horizontal", 0)
bottomEnd = EndLine(screen, "horizontal", MAX_HEIGHT - 1)
verLines.add(leftEnd, rightEnd)
horLines.add(topEnd, bottomEnd)

# game variables
fpstick = FPS * 8
game_run = True
score_left, score_right = 0, 0
font = pg.font.SysFont("Ink Free", 50)
brickNum = 7
bricks = makeBricks(3, brickNum)
for brick in bricks:
    print(brick.rect.center)

winScreen, loseScreen = False, False


def displayWinScreen():
    text_win = font.render("You win!!!", True, GREEN, BLUE)
    text_winRect = text_win.get_rect()
    text_winRect.center = (MAX_WIDTH / 2, MAX_HEIGHT / 2)
    screen.blit(text_win, text_winRect)


def displayLoseScreen():
    text_lose = font.render("You lose!!!", True, GREEN, LUE)
    text_loseRect = text_lose.get_rect()
    text_loseRect.center = (MAX_WIDTH / 2, MAX_HEIGHT / 2)
    screen.blit(text_lose, text_loseRect)


while 1:
    for event in pg.event.get():
        # pressing exit
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(BLACK)
    if pg.key.get_pressed()[pg.K_SPACE]:
        winScreen, loseScreen = False, False
        balls = pg.sprite.Group()
        ball = Ball(screen, 10, MAX_WIDTH / 2, MAX_HEIGHT / 2, randint(-5, 5), -10, RED)
        balls.add(ball)
        bricks = makeBricks(3, brickNum)
        fpstick = FPS * 8
        game_run = True
        bat_B.changeSize(100, bat_B.rect.height)
    if winScreen:
        displayWinScreen()
    elif loseScreen:
        displayLoseScreen()
    if len(bricks) == 0:
        game_run = False
        winScreen = True
    if game_run:
        fpstick -= 1
        if fpstick < 0:
            brickTop = MAX_HEIGHT
            for brick in bricks:
                brick.rect.move_ip(0, 50)
                if brick.rect.bottom > MAX_HEIGHT:
                    game_run = False
                    loseScreen = True
            bricks.add(*makeBricks(1, brickNum))
            ball.vy += 2 * ball.vy / abs(ball.vy)
            newWidth = max(50, bat_B.image.get_width() - 10)
            bat_B.changeSize(newWidth, bat_B.rect.height)
            fpstick = FPS * 8
        for ball in balls:
            balls.remove(ball)
            ball.specialCollide(bat_B, x=False, sensitivity=10)
            ball.inelasticCollide(verLines, y=False)
            endCheck = ball.inelasticCollide(horLines, x=False) or []
            if bottomEnd in endCheck:
                game_run = False
                loseScreen = True
                print("left", ball.vx, ball.vy)
            else:
                ball.inelasticCollide(bricks, kill=True, x=False)
                ball.update()
                balls.add(ball)
    bat_B.update()
    bottomEnd.draw(screen)
    bricks.draw(screen)
    bats.draw(screen)
    balls.draw(screen)
    pg.display.update()
    fpscheck.tick(FPS)
