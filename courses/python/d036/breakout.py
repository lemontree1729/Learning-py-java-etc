import sys
from random import randint

try:
    import pygame as pg
except ModuleNotFoundError:
    print("ModuleError: you should install pg")
    sys.exit(1)


class Ball(pg.sprite.Sprite):
    def __init__(
        self, surface, radius, x_start, y_start, vx_start, vy_start, color=None
    ):
        super().__init__()
        self.maxh = surface.get_height()
        self.maxw = surface.get_width()
        self.image = pg.Surface((radius * 2, radius * 2))
        self.image.set_colorkey(BLACK)
        self.color = color or (randint(0, 255), randint(0, 255), randint(0, 255))
        pg.draw.circle(self.image, self.color, (radius, radius), radius, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (x_start, y_start)
        self.vx, self.vy = vx_start, vy_start
        self.vx_start, self.vy_start = vx_start, vy_start
        self.radius = radius

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.left < 0:
            self.vx *= -1
        if self.rect.right > self.maxw:
            self.vx *= -1
        if self.rect.top < 0:
            self.vy *= -1

    def start(self):
        self.vx = self.vx_start
        self.vy = self.vy_start

    def checkCollide(
        self, group, x=True, y=True, kill=False, collided=pg.sprite.collide_rect
    ):
        if pg.sprite.spritecollide(self, group, kill, collided):
            if x:
                self.vx *= -1
            else:
                self.vx = randint(-10, 10)
            if y:
                self.vy *= -1  # ball should exchange their valocity
            else:
                self.vy = randint(-10, 10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Bat(pg.sprite.Sprite):
    def __init__(self, surface, width, height, x_start, y_start, color):
        super().__init__()
        self.maxh = surface.get_height()
        self.maxw = surface.get_width()
        self.image = pg.Surface((width, height))
        pg.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x_start, y_start)
        self.left = pg.K_LEFT
        self.right = pg.K_RIGHT

    def update(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[self.left]:
                self.rect.move_ip(-20, 0)
        if self.rect.right < self.maxw:
            if pressed_keys[self.right]:
                self.rect.move_ip(20, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class EndLine(pg.sprite.Sprite):
    def __init__(self, surface, direction, pos, color):
        super().__init__()
        self.maxh = surface.get_height()
        self.maxw = surface.get_width()
        if direction == "vertical":
            self.image = pg.Surface((1, self.maxh))
            self.rect = self.image.get_rect()
            self.rect.top = 0
            self.rect.left = pos
        elif direction == "horizontal":
            self.image = pg.Surface((self.maxw, 1))
            self.rect = self.image.get_rect()
            self.rect.top = pos
            self.rect.left = 0
        self.image.fill(color)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def determineSide(rect1, rect2):
    if rect1.midtop[1] > rect2.midtop[1]:
        return "top"
    elif rect1.midleft[0] > rect2.midleft[0]:
        return "left"
    elif rect1.midright[0] < rect2.midright[0]:
        return "right"
    else:
        return "bottom"


##################################################################################

pg.init()

FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MINT = (0, 255, 255)
YELLOW = (255, 255, 0)
MAX_WIDTH, MAX_HEIGHT = 600, 400

fpscheck = pg.time.Clock()
screen = pg.display.set_mode((MAX_WIDTH, MAX_HEIGHT))  # main surface
pg.display.set_caption("Breakout Game")


firstball = Ball(
    screen, radius=12, x_start=288, y_start=188, vx_start=16, vy_start=5
)  # 10
bat_D = Bat(screen, 100, 15, MAX_WIDTH / 2, MAX_HEIGHT - 30, MINT)
bats = pg.sprite.Group()
bats.add(bat_D)
targetbats = pg.sprite.Group()
n = 3
m = 10
for y in range(n):
    for x in range(m):
        targetbats.add(Bat(screen, 40, 15,
        MAX_WIDTH * (x + 1) / (m + 1), MAX_HEIGHT * (y + 1) / (n + 5), GREEN))  # fmt: skip
balls = pg.sprite.Group()
ball = Ball(screen, 10, MAX_WIDTH / 2, MAX_HEIGHT / 2, randint(-10, 10), -10, RED)  # fmt: skip
balls.add(ball)
bottomEnd = EndLine(screen, "horizontal", MAX_HEIGHT - 1, RED)

fpstick = 0
game_start = False
score_left, score_right = 0, 0
font = pg.font.SysFont("Ink Free", 50)

while 1:
    screen.fill(BLACK)
    for event in pg.event.get():
        # pressing exit
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if pg.key.get_pressed()[pg.K_SPACE]:
        balls = pg.sprite.Group()
        ball = Ball(screen, 10, MAX_WIDTH / 2, MAX_HEIGHT / 2, randint(-5, 5), -10, RED)  # fmt: skip
        balls.add(ball)
        targetbats = pg.sprite.Group()
        n = 3
        m = 10
        for y in range(n):
            for x in range(m):
                targetbats.add(Bat(screen, 40, 15,
                MAX_WIDTH * (x + 1) / (m + 1), MAX_HEIGHT * (y + 1) / (n + 5), GREEN))  # fmt: skip
    if len(targetbats) == 0:
        text_win = font.render("You win!!!", True, GREEN, BLUE)
        text_winRect = text_win.get_rect()
        text_winRect.center = (MAX_WIDTH / 2, MAX_HEIGHT / 2)
        screen.blit(text_win, text_winRect)
        pg.display.update()
        fpscheck.tick(FPS)
        continue
    for ball in balls:
        balls.remove(ball)
        ball.checkCollide(targetbats, kill=True, x=False)
        ball.checkCollide(bats, x=False)
        if pg.sprite.collide_rect(ball, bottomEnd):
            print("left")
        else:
            balls.add(ball)
    # make short here!
    bottomEnd.draw(screen)
    bats.update()
    targetbats.draw(screen)
    bats.draw(screen)
    balls.update()
    balls.draw(screen)
    pg.display.update()
    fpscheck.tick(FPS)
