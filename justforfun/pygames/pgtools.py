from abc import ABCMeta, abstractmethod
import pygame as pg
from random import randint


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

    @abstractmethod  # define how to make image
    def makeImage(self):
        pass

    def changeImage(self, image: pg.Surface):
        self.image = image
        temp = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = temp

    # speed limit for preventing penetration
    # @property
    # def vx(self):
    #     return self._vx

    # @vx.setter
    # def vx(self, vx):
    #     self._vx = vx / abs(vx) * min(self.rect.width / 2, abs(vx))

    # @property
    # def vy(self):
    #     return self._vx

    # @vy.setter
    # def vy(self, vy):
    #     self._vy = vy / abs(vy) * min(self.rect.height / 2, abs(vy))

    @property
    def cord(self):
        return self.rect.center

    @property
    def spd(self):
        return (self.vx, self.vy)

    def update(self):
        self.move()

    def move(self):
        boundaryMove = False
        if self.rect.top < 0:
            self.rect.top = 0
            self.vy = abs(self.vy)
            boundaryMove = True
        if self.rect.bottom > self.maxh:
            self.rect.bottom = self.maxh
            self.vy = -abs(self.vy)
            boundaryMove = True
        if self.rect.right > self.maxw:
            self.rect.right = self.maxw
            self.vx = -abs(self.vx)
            boundaryMove = True
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = abs(self.vx)
            boundaryMove = True
        if not boundaryMove:
            self.rect.move_ip(self.vx, self.vy)
        self.collided = False

    def moveOnce(self, vx, vy):
        self.vx, self.vy = vx, vy
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


class Ball(MovingObject):
    def __init__(self, radius, surface=None, cord=None, spd=(0, 0), color=randomBrightRGB()):
        self.radius = radius
        self.multiCollide = False
        self.color = color
        super().__init__(surface, cord, spd)

    def makeImage(self, radius=None, color=None):
        if color != None:
            self.color = color
        if radius != None:
            self.radius = radius
        image = pg.Surface((self.radius * 2, self.radius * 2))
        image.set_colorkey((0, 0, 0))
        pg.draw.circle(image, self.color, (self.radius, self.radius), self.radius, 0)
        return image

    def changeRadius(self, radius):
        self.changeImage(self.makeImage(radius, self.color))


class Bat(pg.sprite.Sprite):
    def __init__(self, size, surface=None, cord=None, spd=(0, 0), color=randomBrightRGB()):
        self.width, self.height = size
        self.color = color

        self.k_up, self.k_down = pg.K_UP, pg.K_DOWN
        self.k_left, self.k_right = pg.K_LEFT, pg.K_RIGHT

    def makeImage(self, width=None, height=None, color=None):
        if color != None:
            self.color = color
        if width != None:
            self.width = width
        if height != None:
            self.height = height
        image = pg.Surface(self.width, self.height)
        pg.draw.rect(image, self.color, (0, 0, width, height))
        return image

    def changeSize(self, radius):
        pass

    # def update(self):
    #     pressed_keys = pg.key.get_pressed()
    #     if self.rect.top > 0:
    #         if self.k_up != None and pressed_keys[self.k_up]:
    #             self.rect.move_ip(0, -20)
    #     if self.rect.bottom < self.maxh:
    #         if self.k_down != None and pressed_keys[self.k_down]:
    #             self.rect.move_ip(0, 20)
    #     if self.rect.left > 0:
    #         if self.k_left != None and pressed_keys[self.k_left]:
    #             self.rect.move_ip(-20, 0)
    #     if self.rect.right < self.maxw:
    #         if self.k_right != None and pressed_keys[self.k_right]:
    #             self.rect.move_ip(20, 0)

    def changeSize(self, width, height):
        temp = self.rect.center
        self.image = pg.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = temp

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class EndLine(pg.sprite.Sprite):
    def __init__(self, surface, direction, pos, color=None):
        super().__init__()
        self.maxh = surface.get_height()
        self.maxw = surface.get_width()
        if direction == "vertical":
            self.image = pg.Surface((1, self.maxh))
            self.rect = self.image.get_rect()
            self.rect.top, self.rect.left = 0, pos
        elif direction == "horizontal":
            self.image = pg.Surface((self.maxw, 1))
            self.rect = self.image.get_rect()
            self.rect.top, self.rect.left = pos, 0
        self.image.fill(color or (255, 255, 255))

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def inelasticCollide(
    origin: MovingObject, group, x=True, y=True, collide=pg.sprite.collide_rect, kill=False, default=True
):
    if not default:
        default = not self.collided
    result = pg.sprite.spritecollide(self, group, kill, collide)
    if result and default:
        self.collided = True
        if x:
            self.vx *= -1
        if y:
            self.vy *= -1
    return result


# ball should exchange their valocity
def elasticCollide(self, target, default=True):
    if not default:
        default = not self.collided
    result = pg.sprite.collide_circle(self, target)
    if result and default:
        x1, y1 = self.rect.center
        x2, y2 = target.rect.center
        rvx, rvy = target.vx - self.vx, target.vy - self.vy
        value = 10000
        c0 = (self.radius + target.radius) ** 2
        xr, yr = 0, 0
        for i in range(5):
            x, y = x2 - x1 - i * rvx / 5, y2 - y1 - i * rvy / 5
            temp = abs(x ** 2 + y ** 2 - c0)
            if temp < value:
                value = temp
                xr, yr = x, y
        nv = pg.math.Vector2(xr, yr)
        # nv = pg.math.Vector2(x2 - x1, y2 - y1) just for simple
        v = pg.math.Vector2(self.vx, self.vy).reflect(nv)
        self.vx, self.vy = v.x, v.y
    return result


def specialCollide(self, target, x=True, y=True, sensitivity=5, default=True):
    if not default:
        default = not self.collided
    result = pg.sprite.collide_rect(self, target)
    if result and default:
        self.collided = True
        if x:
            self.vx *= -1
            ratio = (self.rect.centery - target.rect.centery) / (target.rect.height / 2)
            self.vy = sensitivity * ratio
        if y:
            self.vy *= -1
            ratio = (self.rect.centerx - target.rect.centerx) / (target.rect.width / 2)
            self.vx = sensitivity * ratio
        print("collide", self.vx, self.vy)
    return result
