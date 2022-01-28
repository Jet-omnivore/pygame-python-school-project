import math
import pygame
import time
import sys


class Bezier:
    def __init__(self, points):
        self.points = list(points)
        self.time = 0

    def calculate(self):
        t = self.time
        x1, y1, x2, y2 = self.points

        x = 3 * t * pow(1 - t, 2) * x1 + 3 * t * t * (1 - t) * x2 + pow(t, 3)
        y = 3 * t * pow(1 - t, 2) * y1 + 3 * t * t * (1 - t) * y2 + pow(t, 3)

        return x, y

    def update(self, dt):
        self.time += dt
        if self.time >= 1:
            self.time = 0


window = pygame.display.set_mode((800, 600))
display = pygame.Surface((400, 300))

b = Bezier([0.64, 0.57, 0.67, 1.53])
pos = [40, 40]

s_time = time.time()
dt = 0

while True:

    dt = time.time() - s_time
    s_time = time.time()

    display.fill((0,) * 3)
    b.update(dt)

    x, y = b.calculate()
    slope = math.tan(math.atan2(y, x))
    length = math.hypot(x, y)
    center = (x * 20 + 200, y * 20 + 150)
    pygame.draw.circle(display, (255,) * 3, center, 1)

    cpos = pos.copy()
    cpos[0] += slope * length * 30
    pygame.draw.circle(display, (255,) * 3, cpos, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.transform.scale(display, window.get_size(), window)
    pygame.display.update()
