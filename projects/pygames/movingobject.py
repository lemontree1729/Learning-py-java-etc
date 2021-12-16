import pygame as pg
from random import randint

from pygame.sprite import Group


def randomBrightRGB():
    rgb = 0, 0, 0
    while sum(rgb) < 255:
        rgb = randint(0, 255), randint(0, 255), randint(0, 255)
    return rgb


class MovingObject(pg.sprite.Sprite):
    def __init__(self, surface=None, cord=None, spd=(0, 0)):
        super().__init__()
        surface = surface or pg.display.get_surface()
        self.surface = surface
        self.maxh, self.maxw = surface.get_height(), surface.get_width()
        self.image = self.makeImage()
        self.rect = self.image.get_rect()
        cord = cord or (self.maxw / 2, self.maxh / 2)
        self.x_init, self.y_init = cord
        self.rect.center = cord
        self.vx, self.vy = spd
        self.multiCollide = True
        self.collided = False

    def makeImage(self):
        pass

    def changeImage(self, image: pg.Surface):
        self.image = image
        temp = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = temp

    @property
    def cord(self):
        return self.rect.center

    @property
    def spd(self):
        return (self.vx, self.vy)

    def update(self):
        self.move()

    def move(self):
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.top < 0:
            self.rect.top = 0
            self.vy = abs(self.vy)
        if self.rect.bottom > self.maxh:
            self.rect.bottom = self.maxh
            self.vy = -abs(self.vy)
        if self.rect.right > self.maxw:
            self.rect.right = self.maxw
            self.vx = -abs(self.vx)
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = abs(self.vx)
        self.collided = False

    def moveOnce(self, spd):
        self.vx, self.vy = spd
        self.move()
        self.vx, self.vy = 0, 0

    def start_pos(self):
        self.rect.center = (self.x_init, self.y_init)

    def start(self):
        self.vx, self.vy = self.vx_temp, self.vy_temp

    def stop(self):
        self.vx_temp, self.vy_temp = self.vx, self.vy
        self.vx, self.vy = 0, 0

    def draw(self, surface: pg.Surface):
        surface.blit(self.image, self.rect)

    def xyCollide(self, target, x=True, y=True, weight=0):
        if not self.multiCollide and self.collided:
            return
        result = pg.sprite.collide_rect(self, target)
        if result:
            self.collided = True
            if x:
                self.vx *= -1
                if weight:
                    ratio = (self.rect.centery - target.rect.centery) / (target.rect.height / 2)
                    self.vy = weight * abs(self.vx) * ratio
            if y:
                self.vy *= -1
                if weight:
                    ratio = (self.rect.centerx - target.rect.centerx) / (target.rect.width / 2)
                    self.vx = weight * abs(self.vy) * ratio
            print("xy collide", self.vx, self.vy)
        return result

    def xyGroupCollide(self, group: Group, x=True, y=True, kill=False):
        if not self.multiCollide and self.collided:
            return
        result = pg.sprite.spritecollide(self, group, kill, pg.sprite.collide_rect)
        if result:
            self.collided = True
            if x:
                self.vx *= -1
            if y:
                self.vy *= -1
            print("xygroup collide", self.vx, self.vy)
        return result


class Ball(MovingObject):
    def __init__(self, radius, cord=None, spd=(0, 0), color=None, surface=None):
        self.radius = radius
        self.color = color or randomBrightRGB()
        super().__init__(surface, cord, spd)
        self.multiCollide = False

    def makeImage(self, radius=None, color=None):
        self.radius = radius or self.radius
        self.color = color or self.color
        image = pg.Surface((self.radius * 2, self.radius * 2))
        image.set_colorkey((0, 0, 0))
        pg.draw.circle(image, self.color, (self.radius, self.radius), self.radius, 0)
        return image

    def changeColor(self, color=None):
        self.color = color or randomBrightRGB()
        self.changeImage(self.makeImage(self.radius, self.color))

    def changeRadius(self, radius):
        self.changeImage(self.makeImage(radius, self.color))

    def ballCollide(self, target):  # Collide that acts like a ball
        if not self.multiCollide and self.collided:
            return
        result = pg.sprite.collide_circle(self, target)
        if result:
            self.collided = True
            x1, y1 = self.rect.center
            x2, y2 = target.rect.center
            rvx, rvy = target.vx - self.vx, target.vy - self.vy
            value = 10000
            c0 = (self.radius + target.radius) ** 2
            xr, yr = 0, 0
            for i in range(10):
                x, y = x2 - x1 - i * rvx / 10, y2 - y1 - i * rvy / 10
                temp = abs(x ** 2 + y ** 2 - c0)
                if temp < value:
                    value = temp
                    xr, yr = x, y
            nv = pg.math.Vector2(xr, yr)
            # nv = pg.math.Vector2(x2 - x1, y2 - y1) just for simple
            v = pg.math.Vector2(self.vx, self.vy).reflect(nv)
            self.vx, self.vy = v.x, v.y
            print("ball collide", self.vx, self.vy)
        return result

    def realisticCollide(self, target, accurate=100):  # Most realistic but not fun enough
        if self.collided and target.collided:
            return
        result = pg.sprite.collide_circle(self, target)
        if result:
            self.collided, target.collided = True, True
            originPos = pg.math.Vector2(self.rect.center)
            originSpd = pg.math.Vector2(self.spd)
            targetPos = pg.math.Vector2(target.rect.center)
            targetSpd = pg.math.Vector2(target.spd)
            inaccRelativePos = targetPos - originPos
            relativeSpd = targetSpd - originSpd
            approxValue = 10000  # just big value
            wantedValue = (self.radius + target.radius) ** 2
            n = accurate
            for i in range(n):
                tempPos = inaccRelativePos - i * relativeSpd / n
                tempValue = abs(tempPos.length_squared() - wantedValue)
                if tempValue < approxValue:  # approxValue goes to wantedValue
                    approxValue = tempValue
                    accRelativePos = tempPos
            # nv = pg.math.Vector2(x2 - x1, y2 - y1) just for simple
            reflectOriginSpd = pg.math.Vector2(self.vx, self.vy).reflect(accRelativePos)
            reflectTargetSpd = pg.math.Vector2(target.vx, target.vy).reflect(accRelativePos)
            collideOriginSpd = (originSpd + reflectOriginSpd) / 2 + (targetSpd - reflectTargetSpd) / 2
            collideTargetSpd = (targetSpd + reflectTargetSpd) / 2 + (originSpd - reflectOriginSpd) / 2
            self.vx, self.vy = collideOriginSpd.x, collideOriginSpd.y
            target.vx, target.vy = collideTargetSpd.x, collideTargetSpd.y
            print("realistic collide", self.vx, self.vy)
        return result


class Bat(MovingObject):
    def __init__(self, size, cord=None, spd=(0, 0), color=None, surface=None):
        self.width, self.height = size
        self.color = color or randomBrightRGB()
        self.k_up, self.k_down, self.k_right, self.k_left = (None,) * 4
        super().__init__(surface, cord, spd)

    def makeImage(self, width=None, height=None, color=None):
        self.width = width or self.width
        self.height = height or self.height
        self.color = color or self.color
        image = pg.Surface((self.width, self.height))
        image.fill(self.color)
        return image

    def keyMove(self, tick):
        pressed_keys = pg.key.get_pressed()
        if self.k_up != None and pressed_keys[self.k_up]:
            self.moveOnce((0, -tick))
        if self.k_down != None and pressed_keys[self.k_down]:
            self.moveOnce((0, tick))
        if self.k_left != None and pressed_keys[self.k_left]:
            self.moveOnce((-tick, 0))
        if self.k_right != None and pressed_keys[self.k_right]:
            self.moveOnce((tick, 0))

    def changeSize(self, width, height):
        temp = self.rect.center
        self.image = pg.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = temp

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class BorderLine(MovingObject):
    def __init__(self, direction="vertical", pos=1, thickness=1, color=None, surface=None):
        self.direction = direction
        self.pos = pos
        self.thickness = thickness
        self.color = color or randomBrightRGB()
        surface = surface or pg.display.get_surface()
        if self.direction == "vertical":
            cord = (pos, surface.get_height() / 2)
        elif self.direction == "horizontal":
            cord = (surface.get_width() / 2, pos)
        super().__init__(surface, cord, (0, 0))

    def makeImage(self, direction=None, pos=None, thickness=None, color=None):
        self.direction = direction or self.direction
        self.pos = pos or self.pos
        self.thickness = thickness or self.thickness
        self.color = color or self.color
        if self.direction == "vertical":
            image = pg.Surface((self.thickness, self.maxh))
        elif self.direction == "horizontal":
            image = pg.Surface((self.maxw, self.thickness))
        image.fill(self.color)
        return image

    def draw(self, surface):
        surface.blit(self.image, self.rect)
