import pygame
import math

from enum import Enum, auto

ACCEL_DUE_TO_GRAVITY = 10  # not negative because in pygame y axis flipped
PARTICLE_DEAD_MULT = 0.2


class ProjType(Enum):
    NOPATH = auto()
    PATH = auto()


class ProjectileManager:
    def __init__(self, world):
        self.projectiles = []
        self.world = world

    def update(self):
        font = self.world.engine.font
        tilemap = self.world.tilemap
        dt = self.world.engine.dt
        display = self.world.engine.display
        for i, projectile in reversed(list(enumerate(self.projectiles))):
            if not projectile.is_alive():
                self.projectiles.pop(i)
            projectile.update(dt, tilemap)
            projectile.render(display, font, dt)

    def add_projectile(self, pos, velocity, ptype=ProjType.PATH):
        new_projectile = Projectile(pos, velocity, ptype)
        self.projectiles.append(new_projectile)


class Projectile:

    def __init__(self, pos, velocity, ptype, timer=10):
        self.pos = list(pos)
        self.start_pos = list(pos)
        self.velocity = list(velocity)
        self.timer = timer
        self.path = [self.pos.copy()]
        self.type = ptype
        self.time = 0

        self.text_pos = [[0, 0], [0, 0]]  # horizontal vertical

    def render(self, surf, font, dt):
        radius = int(abs(self.timer) / 2)
        pygame.draw.circle(surf, (174, 50, 50), self.pos, radius)

        self.draw_horizontal_range(surf, font, dt)
        self.draw_vertical_range(surf, font, dt)
        self.draw_velocity(surf)
        if self.type is ProjType.PATH:
            self.render_path(surf)

    def render_path(self, surf):
        pygame.draw.lines(surf, (255, 255, 255), False, self.path)
        if len(self.path) > 70:
            self.path.pop(0)

    def draw_horizontal_range(self, surf, font, dt=1/60):
        dt *= 60
        start_pos = [self.start_pos[0], 236]
        end_pos = [self.pos[0], 236]
        pygame.draw.line(surf, (215, 82, 186), start_pos, end_pos)
        pointer = [[end_pos[0], end_pos[1] + 3], [end_pos[0], end_pos[1] - 3]]
        pygame.draw.line(surf, (15, 82, 186), *pointer, 3)

        dist = int(math.dist(start_pos, end_pos))

        if any(self.velocity):
            self.text_pos[0] = [start_pos[0] + dist / 2, 235]
        else:
            self.text_pos[0][0] = min(self.text_pos[0][0] + 0.5 * dt, end_pos[0])
        font.render(f"{dist}", self.text_pos[0], (215, 82, 186))

    def draw_vertical_range(self, surf, font, dt):
        dt *= 60
        start_pos = [self.start_pos[0], 236]
        end_pos = [self.start_pos[0], self.pos[1]]
        pygame.draw.line(surf, (15, 82, 186), start_pos, end_pos)
        pointer = [[end_pos[0] - 3, end_pos[1]], [end_pos[0] + 3, end_pos[1]]]
        pygame.draw.line(surf, (15, 82, 186), *pointer, 3)

        dist = int(math.dist(start_pos, end_pos))
        if any(self.velocity):
            self.text_pos[1] = [start_pos[0], end_pos[1] + dist / 2]
        else:
            self.text_pos[1][0] = min(self.text_pos[1][1] + 0.5 * dt, end_pos[1])
        font.render(f"{dist}", self.text_pos[1], (215, 82, 186))

    def draw_velocity(self, surf):
        end_pos = [pos + vel for pos, vel in zip(self.pos, self.velocity)]
        pygame.draw.line(surf, (174, 50, 50), self.pos, end_pos)

    def tile_collide(self, tile_map: dict, tile_size):
        check_pos = (self.pos[0] // tile_size, self.pos[1] // tile_size)
        return check_pos in tile_map

    def update(self, dt, tile_map):
        tile_size = tile_map.rect_tile_size

        self.velocity[1] += ACCEL_DUE_TO_GRAVITY * dt

        self.pos[0] += self.velocity[0] * dt
        if self.tile_collide(tile_map.map, tile_size):
            self.velocity = [0, 0]
            self.velocity[0] *= -1
            self.pos[0] += self.velocity[0] * dt

        self.pos[1] += self.velocity[1] * dt
        if self.tile_collide(tile_map.map, tile_size):
            self.velocity = [0, 0]
            self.velocity[1] *= -1
            self.pos[1] += self.velocity[1] * dt

        if self.type is ProjType.PATH:
            self.path.append(self.pos.copy())

        self.timer -= dt * PARTICLE_DEAD_MULT

        '''
        t = self.time
        x = self.velocity[0] * t

        tile_size = tile_map.rect_tile_size
        new_x = self.start_pos[0] + x
        new_pos = (new_x // tile_size, self.pos[1] // tile_size)

        if new_pos in tile_map.map:
            print('yes')
            self.velocity[0] *= -0.5

        y = self.velocity[1] * t + (0.5 * ACCEL_DUE_TO_GRAVITY * t * t)

        new_y = self.start_pos[1] + y
        new_pos = (int(self.pos[0] // tile_size), int(new_y // tile_size))
        if new_pos in tile_map.map:
            print('yes')
            self.velocity[1] *= -1

        self.pos[0] = x + self.start_pos[0]
        self.pos[1] = y + self.start_pos[1]

        if self.type is ProjType.PATH:
            self.path.append(self.pos.copy())

        self.timer -= dt * PARTICLE_DEAD_MULT
        self.time += dt
        '''

    def is_alive(self):
        return self.timer > 0
