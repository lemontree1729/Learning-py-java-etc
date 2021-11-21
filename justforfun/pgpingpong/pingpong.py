import sys

try:
    import pygame
except ModuleNotFoundError:
    print("you should install pygame")
pygame.init()

FPS = 30
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
fpscheck = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))
screen.fill(BLACK)
pygame.display.set_caption("PingPong Game")
pygame.draw.line(screen, GREEN, (screen.get_width() / 2, 0),
 (screen.get_width() / 2, screen.get_height()))  # fmt: skip

while 1:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    fpscheck.tick(FPS)
