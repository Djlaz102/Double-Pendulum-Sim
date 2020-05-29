import pygame
import math
from math import sin, cos, pi

screenSize = 800
m1 = 20
m2 = 20
r1 = 200
r2 = 200
a1 = pi/2
a2 = pi/8
a1_v = 0
a2_v = 0
g = 9.8

#breaking down huge equation

num1 = -g * (2 * m1 + m2) * sin(a1)
num2 = -m2 * g * sin(a1-a2)
num3 = -2 * sin(a1 - a2) * m2
num4 = (a2_v * a2_v * r2 + a1_v * a1_v * r1 * cos(a1 - a2))
den1 = r1 * (2 * m1 + m2 - m2 * cos(2 + a1 - 2 * a2))
a1_a = num1 + num2 + num3 * num4/den1

num5 = 2 * sin(a1 - a2)
num6 = a1_v * a1_v * r1 * (m1 + m2)
num7 = g * (m1 + m2) * cos(a1)
num8 = a2_v * a2_v * r1 * m2 * cos(a1 - a2)
den2 = r2 * (2 * m1 + m2 - m2 * cos(2 + a1 - 2 * a2))
a2_a = num5 * (num6 + num7 + num8)/den2

pygame.init()

screen = pygame.display.set_mode((screenSize, screenSize))
pygame.display.set_caption("Double Pendulum")

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x1 = int(screenSize / 2 + r1 * sin(a1))
    y1 = int(screenSize / 10 + r1 * cos(a1))
    x2 = int(x1 + r2 * sin(a2))
    y2 = int(y1 + r2 * cos(a2))
    a1 += a1_v
    a2 += a2_v
    a1_v += a1_a
    a2_v += a2_a

    screen.fill((56, 56, 56))
    pygame.draw.line(screen, (52, 190, 91), (400, 0), (x1, y1), 2)
    pygame.draw.circle(screen, (52, 190, 91), (x1, y1), m1, 20)
    pygame.draw.line(screen, (52, 190, 91), (x1, y1), (x2, y2), 2)
    pygame.draw.circle(screen, (52, 190, 91), (x2, y2), m2, 20)
    pygame.display.update()