import sys
from random import randint

try:
    import pygame as pg
except ModuleNotFoundError:
    print("ModuleError: you should install pg")
    sys.exit(1)

pg.init()

FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MINT = (0, 255, 255)
YELLOW = (255, 255, 0)
MAX_WITDH, MAX_HEIGHT = 600, 400

fpscheck = pg.time.Clock()
screen = pg.display.set_mode((MAX_WITDH, MAX_HEIGHT))  # main surface
pg.display.set_caption("PingPong Game")


class Ball(pg.sprite.Sprite):
    def __init__(
        self, surface, radius, x_start, y_start, vx_start, vy_start, color=None
    ):
        super().__init__()
        self.surface = surface
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
        if self.rect.bottom > self.maxh:
            self.vy *= -1
        if self.rect.top < 0:
            self.vy *= -1

    def start(self):
        self.vx = self.vx_start
        self.vy = self.vy_start

    def checkCollide(self, group, x=True, y=True, collided=pg.sprite.collide_rect):
        if pg.sprite.spritecollide(self, group, False, collided):
            print(self, pg.sprite.spritecollide(self, group, False, collided)[0])
            if x:
                self.vx *= -1
            if y:
                self.vy *= -1  # ball should exchange their valocity

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
        self.up = pg.K_UP
        self.down = pg.K_DOWN

    def update(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[self.up]:
                self.rect.move_ip(0, -20)
        if self.rect.bottom < self.maxh:
            if pressed_keys[self.down]:
                self.rect.move_ip(0, 20)

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


class Edge(pg.sprite.Sprite):
    def __init__(self, surface, x_start=None, y_start=None):
        super().__init__()


firstball = Ball(
    screen, radius=12, x_start=288, y_start=188, vx_start=16, vy_start=5
)  # 10
bat_R = Bat(screen, 15, 100, 575, MAX_HEIGHT / 2, YELLOW)
bat_L = Bat(screen, 15, 100, 25, MAX_HEIGHT / 2, MINT)  # 15, 100, 20, 150, MINT
bat_L.up, bat_L.down = pg.K_w, pg.K_s
bats = pg.sprite.Group()
bats.add(bat_L, bat_R)
balls = pg.sprite.Group()
# wall =
leftEnd = EndLine(screen, "vertical", 0, RED)
rightEnd = EndLine(screen, "vertical", MAX_WITDH - 1, BLUE)

fpstick = 0
game_start = False
score_left, score_right = 0, 0
font = pg.font.SysFont("Ink Free", 50)
displayupdate = True
while 1:
    for event in pg.event.get():
        # pressing exit
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if score_left >= 50 or score_right >= 50:
        score_left, score_right = 0, 0
        displayupdate = False  # stop ball
    if pg.key.get_pressed()[pg.K_SPACE]:
        score_left, score_right = 0, 0
        displayupdate = True
        game_start = True
        fpstick = 30
        balls = pg.sprite.Group()
    if game_start:
        fpstick += 1
    cnt = fpstick / 30
    if cnt >= 1:
        vx, vy = (2 * randint(0, 1) - 1) * randint(10, 15), randint(0, 10)
        balls.add(Ball(screen, 10, 280, 180, vx, vy))
        fpstick = 0
    screen.fill(BLACK)

    for ball in balls:
        balls.remove(ball)
        ball.checkCollide(balls, collided=pg.sprite.collide_circle_ratio(0.5))
        ball.checkCollide(bats, y=False)
        if pg.sprite.collide_rect(ball, leftEnd):
            print("left")
            score_left += 1
        elif pg.sprite.collide_rect(ball, rightEnd):
            print("right")
            score_right += 1
        else:
            balls.add(ball)

    # make short here!
    text_left = font.render(str(score_left), True, GREEN, BLUE)
    text_right = font.render(str(score_right), True, GREEN, BLUE)
    text_leftRect = text_left.get_rect()
    text_leftRect.left = 0
    text_leftRect.top = 0
    text_rightRect = text_right.get_rect()
    text_rightRect.right = MAX_WITDH
    text_rightRect.top = 0
    screen.blit(text_left, text_leftRect)
    screen.blit(text_right, text_rightRect)
    leftEnd.draw(screen)
    rightEnd.draw(screen)
    bats.update()
    bats.draw(screen)
    if displayupdate:
        balls.update()
        balls.draw(screen)

    pg.draw.line(screen, GREEN, (MAX_WITDH / 2, 0), (MAX_WITDH / 2, MAX_HEIGHT))
    pg.display.update()
    fpscheck.tick(FPS)
