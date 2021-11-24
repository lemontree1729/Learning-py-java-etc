import pygame as pg
from random import randint


class Ball(pg.sprite.Sprite):
    def __init__(
        self, surface, radius, x_start, y_start, vx_start, vy_start, color=None
    ):
        super().__init__()
        self.surface = surface
        self.maxh = surface.get_height()
        self.maxw = surface.get_width()
        self.image = pg.Surface((radius * 2, radius * 2))
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
