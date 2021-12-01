# to do
# make SCREEN that shows tracking line of two balls' center
# make screens(title -> press any key, mode SCREEN(vs player, vs computer easy mode, hard mode, physical engine) , key operation SCREEN, )
# (doing) make MovingSprite class
# make groupcollide and normal collide
# make collide more realistic(using double draw of collide point and after move)


import sys
from random import randint
from pygame.constants import KEYDOWN
from pygame.font import Font
from movingobject import *

# make error if pygame is not installed
try:
    import pygame as pg
except ModuleNotFoundError:
    print("ModuleError: you should install pg")
    sys.exit(1)

pg.init()  # <-------------- initialize pygame
pg.display.set_caption("Balls and Bricks")

########## common ############
# global variables
FPS = 30
PURPLE = (102, 0, 153)
DARKBLUE = (0, 0, 139)
SKYBLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MINT = (0, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
MAX_WIDTH, MAX_HEIGHT = 600, 400
BIGINKFONT = pg.font.SysFont("Ink Free", 50)
SMALLCAMBRIAFONT = pg.font.SysFont("Cambria", 25)
SMALLARIALFONT = pg.font.SysFont("Arial", 25)
SMALLGEORGIAFONT = pg.font.SysFont("Gerogia", 25)
FPSCHECK = pg.time.Clock()
SCREEN = pg.display.set_mode((MAX_WIDTH, MAX_HEIGHT))  # main surface
PINGPONGTICK = 3 * FPS
BREAKOUTTICK = 8 * FPS
fpstick = -7  # give minus tick to check whether init or not
titletick = 1.5 * FPS

# ball group
titleBall = Ball(15, (450, 150), (0, -10), RED)
balls = pg.sprite.Group()

# bat group
bats = pg.sprite.Group()

# borderline group
borderLines = pg.sprite.Group()
topEnd = BorderLine("horizontal", 0)
bottomEnd = BorderLine("horizontal", MAX_HEIGHT - 1)
leftEnd = BorderLine("vertical", 0)
rightEnd = BorderLine("vertical", MAX_WIDTH - 1)
borderLines.add(topEnd, bottomEnd, rightEnd, leftEnd)

# screen variables
titleScreen = True
menuScreen = False
manualScreen = False
pingpongScreen = False
breakoutScreen = False
forfunScreen = False

# define event type to get
pg.event.set_blocked(None)
pg.event.set_allowed(pg.QUIT)
pg.event.set_allowed(pg.KEYDOWN)
pg.event.set_allowed(pg.MOUSEBUTTONDOWN)


def showText(SCREEN: pg.Surface, font: Font, text, center, color, background):
    text = font.render(str(text), True, color, background)
    textRect = text.get_rect()
    textRect.center = center
    return SCREEN.blit(text, textRect)


def keyToggle(events, key):
    for event in events:
        if event.type == pg.KEYDOWN and pg.key.get_pressed()[key]:
            return (False, True)


def mouseOver(rect: pg.Rect, cursor):
    if rect.collidepoint(pg.mouse.get_pos()):
        pg.mouse.set_cursor(cursor)


def mouseToggle(rect: pg.Rect):
    if rect.collidepoint(pg.mouse.get_pos()):
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        if pg.mouse.get_pressed()[0]:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
            return (False, True)


########## pingpong ###########
def pingpongInit():
    global fpstick, pingpongPause, score_left, score_right, bat_R, bat_L, bats, balls
    fpstick = PINGPONGTICK
    pingpongPause = True
    score_left, score_right = 5, 5
    bat_R = Bat(size=(10, 100), cord=(575, MAX_HEIGHT / 2), color=YELLOW)
    bat_R.k_up, bat_R.k_down = pg.K_UP, pg.K_DOWN
    bat_L = Bat(size=(10, 100), cord=(25, MAX_HEIGHT / 2), color=MINT)
    bat_L.k_up, bat_L.k_down = pg.K_w, pg.K_s
    bats = pg.sprite.Group()
    bats.add(bat_L, bat_R)
    balls = pg.sprite.Group()
    balls.add(Ball(10, spd=(randint(-5, 5), -10), color=RED))


def pingpongEnd():
    global score_left, score_right
    if score_left <= 0 or score_right <= 0:
        if score_left > score_right:
            showText(SCREEN, BIGINKFONT, "Left win!!!", (MAX_WIDTH / 2, MAX_HEIGHT / 2), GREEN, BLUE)
        elif score_left < score_right:
            showText(SCREEN, BIGINKFONT, "Right win!!!", (MAX_WIDTH / 2, MAX_HEIGHT / 2), GREEN, BLUE)
        else:
            showText(SCREEN, BIGINKFONT, "Draw!!!", (MAX_WIDTH / 2, MAX_HEIGHT / 2), GREEN, BLUE)
        return True
    return False


def computerMove(tick):
    if not balls:
        return
    ball = min(balls, key=lambda x: abs(x.rect.left - bat_L.rect.right))
    if ball.rect.centerx >= MAX_WIDTH / 2:
        return
    center = ball.rect.centery
    if bat_L.rect.top > center:
        bat_L.moveOnce((0, -tick))
    elif bat_L.rect.bottom < center:
        bat_L.moveOnce((0, tick))
    else:
        if bat_L.rect.centery > center + tick:
            bat_L.moveOnce((0, -tick))
        elif bat_L.rect.centery < center - tick:
            bat_L.moveOnce((0, tick))


############### brick ##############
def breakoutInit():
    global fpstick, brickNum, breakoutPause, bat_B, bats, balls, bricks, colorcnt
    fpstick = BREAKOUTTICK
    brickNum = 7
    breakoutPause = True
    bat_B = Bat((100, 15), (MAX_WIDTH / 2, MAX_HEIGHT - 30), color=MINT)
    bat_B.k_right, bat_B.k_left = pg.K_RIGHT, pg.K_LEFT
    bats = pg.sprite.Group()
    bats.add(bat_B)
    balls = pg.sprite.Group()
    balls.add(Ball(10, spd=(randint(-5, 5), -10), color=RED))
    bricks = makeBricks(3, brickNum)
    colorcnt = 0


def breakoutEnd():
    global bricks, balls
    if len(bricks) == 0:
        showText(SCREEN, BIGINKFONT, "You win!!!", (MAX_WIDTH / 2, MAX_HEIGHT / 2), GREEN, BLUE)
        return True
    elif len(balls) == 0:
        showText(SCREEN, BIGINKFONT, "You lose!!!", (MAX_WIDTH / 2, MAX_HEIGHT / 2), GREEN, BLUE)
        return True
    else:
        for brick in bricks:
            if brick.rect.bottom > MAX_HEIGHT:
                showText(SCREEN, BIGINKFONT, "You lose!!!", (MAX_WIDTH / 2, MAX_HEIGHT / 2), GREEN, BLUE)
                return True
        return False


def makeBricks(n, m, color=None):
    bricks = pg.sprite.Group()
    for y in range(n):
        for x in range(m):
            brick = Bat((MAX_WIDTH / (m + 1) - 20, 15), (MAX_WIDTH * (x + 1) / (m + 1), 50 * (y + 1)), color=color)
            bricks.add(brick)
    return bricks


################ for fun #########
def forfunInit():
    global forfunPause, tracer, lastBall, balls
    forfunPause = True
    tracer = []
    lastBall = Ball(10, spd=(randint(-15, 15), randint(-15, 15)), color=RED)
    balls = pg.sprite.Group()
    balls.add(lastBall)


#################### main part ##################
while 1:
    ### exit check
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    ### title screen
    if titleScreen:
        SCREEN.fill(BLACK)
        titleScreen, manualScreen = keyToggle(events, pg.K_SPACE) or (titleScreen, manualScreen)
        bat1 = Bat((150, 15), (450, 50), color=BLUE)
        bat2 = Bat((150, 15), (450, 250), color=BLUE)
        bats.add(bat1, bat2)
        titleBall.xyGroupCollide(bats)
        titleBall.update()
        bats.draw(SCREEN)
        titleBall.draw(SCREEN)
        showText(SCREEN, SMALLGEORGIAFONT, "@Made by SYJ", (70, 30), GRAY, BLACK)
        showText(SCREEN, BIGINKFONT, "Balls and", (170, 110), RED, BLACK)
        showText(SCREEN, BIGINKFONT, "Bricks", (170, 190), BLUE, BLACK)
        titletick -= 1
        if titletick > 0.5 * FPS:
            showText(SCREEN, SMALLARIALFONT, "press <SPACEBAR> to continue", (MAX_WIDTH / 2, 350), WHITE, BLACK)
        if titletick < 0:
            titletick = 1.5 * FPS

    elif manualScreen:
        SCREEN.fill(GRAY)
        showText(SCREEN, BIGINKFONT, "How to Play", (MAX_WIDTH / 2, 50), SKYBLUE, GRAY)
        showText(SCREEN, SMALLCAMBRIAFONT, "Move: <Arrow keys>", (210, 110), PURPLE, GRAY)
        showText(SCREEN, SMALLCAMBRIAFONT, "Pause/Resume: <Spacebar>", (247, 150), PURPLE, GRAY)
        showText(SCREEN, SMALLCAMBRIAFONT, "Restart: <F5>", (170, 190), PURPLE, GRAY)
        showText(SCREEN, SMALLCAMBRIAFONT, "Go to menu: <Backspace>", (235, 230), PURPLE, GRAY)
        showText(SCREEN, SMALLCAMBRIAFONT, "Make balls(in For fun): <Click>", (265, 270), PURPLE, GRAY)
        showText(SCREEN, SMALLARIALFONT, "press <SPACEBAR> to continue", (MAX_WIDTH / 2, 350), BLACK, GRAY)

        manualScreen, menuScreen = keyToggle(events, pg.K_SPACE) or (manualScreen, menuScreen)
    ### menu screen
    elif menuScreen:
        SCREEN.fill(BLACK)
        pingpongMenu = showText(SCREEN, BIGINKFONT, "Pingpong Game", (MAX_WIDTH / 2, 100), RED, BLUE)
        breakoutMenu = showText(SCREEN, BIGINKFONT, "Breakout Game", (MAX_WIDTH / 2, 200), YELLOW, BLUE)
        forfunMenu = showText(SCREEN, BIGINKFONT, "Just for fun", (MAX_WIDTH / 2, 300), GREEN, BLUE)
        mouseOver(SCREEN.get_rect(), pg.SYSTEM_CURSOR_ARROW)
        menuScreen, pingpongScreen = mouseToggle(pingpongMenu) or (menuScreen, pingpongScreen)
        menuScreen, breakoutScreen = mouseToggle(breakoutMenu) or (menuScreen, breakoutScreen)
        menuScreen, forfunScreen = mouseToggle(forfunMenu) or (menuScreen, forfunScreen)

    ### pingpong screen
    elif pingpongScreen:
        SCREEN.fill(BLACK)
        if pg.key.get_pressed()[pg.K_F5] or fpstick < -5:
            pingpongInit()
        if keyToggle(events, pg.K_BACKSPACE):
            pingpongScreen, menuScreen = False, True
            pingpongPause = True
            fpstick = -7
        for event in events:
            if event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_SPACE]:
                pingpongPause = not pingpongPause
        if pingpongEnd():
            pingpongPause = True
        elif pingpongPause:
            showText(SCREEN, SMALLARIALFONT, "<PAUSED>", (MAX_WIDTH / 2, MAX_HEIGHT / 2), GRAY, BLACK)
        if not pingpongPause:
            fpstick -= 1
            if fpstick == -1 and len(balls) < 80:
                spd = (2 * randint(0, 1) - 1) * randint(10, 15), randint(3, 10)
                balls.add(Ball(10, (300, 200), spd))
                fpstick = PINGPONGTICK  # add balls for every 30 fps ticks
            leftDeadBalls = len(leftEnd.xyGroupCollide(balls, kill=True))
            rightDeadBalls = len(rightEnd.xyGroupCollide(balls, kill=True))
            if leftDeadBalls > 0 or rightDeadBalls > 0:
                score_left -= leftDeadBalls
                score_right -= rightDeadBalls
            for ball in balls:  # select ball
                balls.remove(ball)
                ball.xyGroupCollide(bats, y=False)
                for otherball in balls:
                    ball.ballCollide(otherball)  # ellastic collide
                balls.add(ball)
                ball.update()
        # bat update should be here because it should move whether game stops or not!
        bat_R.keyMove(20)
        computerMove(10)
        # bat_L.keyMove(20)
        # drawing part
        showText(SCREEN, BIGINKFONT, score_left, (20, 20), GREEN, BLUE)
        showText(SCREEN, BIGINKFONT, score_right, (MAX_WIDTH - 20, 20), GREEN, BLUE)
        borderLines.draw(SCREEN)
        BorderLine("vertical", MAX_WIDTH / 2, color=GREEN).draw(SCREEN)
        balls.draw(SCREEN)
        bats.draw(SCREEN)

    ### breakout screen
    elif breakoutScreen:
        SCREEN.fill(BLACK)
        if pg.key.get_pressed()[pg.K_F5] or fpstick < -5:
            breakoutInit()
        if keyToggle(events, pg.K_BACKSPACE):
            breakoutScreen, menuScreen = False, True
            breakoutPause = True
            fpstick = -7
        for event in events:
            if event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_SPACE]:
                breakoutPause = not breakoutPause
        if breakoutEnd():
            breakoutPause = True
        elif breakoutPause:
            showText(SCREEN, SMALLARIALFONT, "<PAUSED>", (MAX_WIDTH / 2, MAX_HEIGHT / 2), GRAY, BLACK)
        if not breakoutPause:
            fpstick -= 1
            if fpstick == -1:
                for brick in bricks:
                    brick.moveOnce((0, 50))
                bricks.add(*makeBricks(1, brickNum))
                ball.vy += 2 * ball.vy / abs(ball.vy)
                bat_B.changeSize(max(50, bat_B.image.get_width() - 10), bat_B.rect.height)
                fpstick = BREAKOUTTICK
            bottomEnd.xyGroupCollide(balls, kill=True)
            for ball in balls:
                if colorcnt > 0:
                    colorcnt -= 1
                    ball.changeColor()
                else:
                    ball.changeColor(RED)
                balls.remove(ball)
                ball.xyCollide(bat_B, x=False, weight=1.3)
                if ball.xyGroupCollide(bricks, x=False, kill=True):
                    colorcnt = 1 * FPS
                ball.update()
                balls.add(ball)
        bat_B.keyMove(20)
        borderLines.draw(SCREEN)
        bricks.draw(SCREEN)
        bats.draw(SCREEN)
        balls.draw(SCREEN)
    elif forfunScreen:
        SCREEN.fill(BLACK)
        if pg.key.get_pressed()[pg.K_F5] or fpstick < -5:
            forfunInit()
        if keyToggle(events, pg.K_BACKSPACE):
            forfunScreen, menuScreen = False, True
            forfunPause = True
            fpstick = -7
        for event in events:
            if event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_SPACE]:
                forfunPause = not forfunPause
        if not forfunPause:
            fpstick = 0
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    tracer = []
                    lastBall = Ball(10, cord=pg.mouse.get_pos(), spd=(randint(-15, 15), randint(-15, 15)))
                    balls.add(lastBall)
            for ball in balls:
                balls.remove(ball)
                for otherball in balls:
                    ball.realisticCollide(otherball)
                balls.add(ball)
            balls.update()
            tracer.append(lastBall.rect.center)
        else:
            showText(SCREEN, SMALLARIALFONT, "<PAUSED>", (MAX_WIDTH / 2, MAX_HEIGHT / 2), GRAY, BLACK)
        for center in tracer:
            pg.draw.circle(SCREEN, randomBrightRGB(), center, 2)
        balls.draw(SCREEN)
    # update display and wait for tick
    pg.display.update()
    FPSCHECK.tick(FPS)
