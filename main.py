import pygame
import math
from math import sin, cos, pi

m1 = 10
m2 = 10
r1 = 200
r2 = 200
a1 = 0
a2 = 0
x1 = int(r1 * sin(a1))
y1 = int(r1 * cos(a1))
x2 = int(r2 * sin(a2))
y2 = int(r2 * cos(a2))

pygame.init()

screenSize = 800
screen = pygame.display.set_mode((screenSize, screenSize))
pygame.display.set_caption("Double Pendulum")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 0, 255), (x1, y1), m1, 5)
    pygame.draw.circle(screen, (0, 0, 255), (x2, y2), m2, 5)
    pygame.display.update()