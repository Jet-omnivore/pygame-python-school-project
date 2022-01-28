import pygame
import sys
import math
import time

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONUP, K_k
from random import randint

pygame.init()

display_size = (960, 540)
window = pygame.display.set_mode([int(x) for x in display_size])
display = pygame.Surface(display_size)


def load_img(path):
    img = pygame.image.load(path)
    img.set_colorkey((0, 0, 0))
    return img.copy()


def radians_to_deg(angle):
    return angle * 180 / math.pi

# loading images


shooter = load_img('shooter.png')
shooter = pygame.transform.scale(shooter, (48, 22))
base_canon = load_img('base.png')
base_canon = pygame.transform.scale(base_canon, (40, 40))
projectile = load_img('projectile.png')
projectile = pygame.transform.scale(projectile, (14, 10))


TILE_SIZE = 20
tile_map = {
        # (5, 5): (255, 0, 0),
        # (5, 6): (255, 0, 0),
        # (5, 7): (255, 0, 0),
        # (5, 8): (255, 0, 0),
        # (6, 8): (255, 0, 0),
        # (7, 8): (255, 0, 0),
        # (8, 8): (255, 0, 0),
        # (9, 8): (255, 0, 0),
        # (9, 8): (255, 0, 0),
        # (10, 8): (255, 0, 0),
        # (11, 8): (255, 0, 0),
        # (12, 8): (255, 0, 0),
        # (12, 7): (255, 0, 0),
        # (12, 6): (255, 0, 0),
        # (12, 5): (255, 0, 0),
        # (12, 4): (255, 0, 0),
        }


class Particle:

    def __init__(self, pos: list, velocity: list, draw_path=False) -> None:
        self.pos = list(pos)
        self.velocity = list(velocity)
        self.alive = True
        self.angle = 0
        self.timer = 20
        self.draw_path = draw_path
        self.path = [self.pos.copy()]
        self.initial_pos = list(pos)
        self.distance = [0, 0]  # horizontal and vertical distance

    def render(self):
        radius = int(abs(self.timer) / 2)
        pygame.draw.circle(display, (172, 50, 50), self.pos, radius)
        self.draw_vector()

    def draw_vector(self):
        hypot = math.sqrt(self.velocity[1] ** 2 + self.velocity[0] ** 2)
        pygame.draw.line(display, (172, 50, 50), self.pos, (self.pos[0] + math.cos(self.angle) * hypot * 10,self.pos[1] + math.sin(self.angle) * hypot * 10))

    def tile_collide(self):
        particle_pos = self.pos[0] // TILE_SIZE, self.pos[1] // TILE_SIZE
        return particle_pos in tile_map

    def render_path(self):
        pygame.draw.lines(display, (255, 255, 255), False, self.path)

    def update(self, dt):
        self.velocity[1] += 0.005 * dt * 360  # gravity
        self.angle = math.atan2(self.velocity[1], self.velocity[0])

        if self.draw_path:
            self.path.append(self.pos.copy())
            self.render_path()
            if len(self.path) > 200:
                pass
                # self.path.pop(0)

        self.pos[0] += self.velocity[0] * dt * 180
        if self.tile_collide():
            self.velocity = [0, 0]
        self.pos[1] += self.velocity[1] * dt * 180
            # self.pos[0] -= self.velocity[0]
            # self.velocity[0] *= -0.75  # x bounciness

        # if self.tile_collide():
            # self.pos[1] -= self.velocity[1]
            # self.velocity[1] *= -0.75  # y bounciness


        self.distance = [(a - b) for a, b in zip(self.pos, self.initial_pos)]
        self.timer -= dt
        if self.timer < 3:
            self.alive = False


particles = []
dt = 0
start_time = time.time()
clock = pygame.time.Clock()


grid_width = 56
grid_height = 27
for x in range(grid_width):
    for y in range(grid_height):
        if y == (grid_height - 1):
            tile_map[(x, y)] = (255, 0, 0)

click_pos = (0, 0)
can_add_new_particle = True


canon_pos = [33 * 2, 259 * 2 - 32]
print(canon_pos)
shooter_pos = [86, 215 + 264]
# [86, 215], [66, 222]
[66, 486]

click = False
k_pressed = False
screen_shake_timer = 0

font = pygame.font.SysFont('courier new', 80)

while True:

    display.fill((120, 146, 158))
    # display.fill((255, 213, 187))

    current_time = time.time()
    dt = current_time - start_time
    start_time = current_time
    screen_shake_timer -= dt

    for tile in tile_map:
        tile_x, tile_y = tile[0] * TILE_SIZE, tile[1] * TILE_SIZE
        rect = (tile_x, tile_y, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(display, tile_map[tile], rect)

    for i, particle in reversed(list(enumerate(particles))):
        if not particle.alive:
            particles.pop(i)
        h_dist, v_dist = particle.distance
        h_dist = int(h_dist / 40)
        v_dist = int(v_dist / 40)
        h_text, v_text = font.render(str(h_dist), False, (255, ) * 3), font.render(str(v_dist), 0, (255, ) * 3)
        display.blit(h_text, (30, i * 10 + 50))
        display.blit(v_text, (60, i * 10 + 50))
        particle.render()
        particle.update(dt)

    mx, my = pygame.mouse.get_pos()

    # canon
    display.blit(base_canon, canon_pos)
    img_half_width, img_half_height = shooter.get_height() / 2, shooter.get_width() / 2
    canon_angle = math.atan2(my - shooter_pos[1], mx - shooter_pos[0])
    canon_angle = min(max(canon_angle, -math.pi / 2), 0)
    rotated_img = pygame.transform.rotate(shooter, -radians_to_deg(canon_angle))


    angle_text = font.render(f'{-int(canon_angle * 180 / math.pi)}', False, (255, 255, 255))
    display.blit(angle_text, (115, 195))
    pygame.draw.arc(display, (255, 255, 255), (62, 195, 50, 50), 0, -canon_angle + 0.05)
    display.blit(rotated_img, [shooter_pos[0] - rotated_img.get_width() // 2, shooter_pos[1] - rotated_img.get_height() // 2])


    if click or k_pressed:
        particle_pos = [
                shooter_pos[0] + math.cos(canon_angle),
                shooter_pos[1] + math.sin(canon_angle)
                ]
        velocity = [
                math.cos(canon_angle) * 10 / 4,
                math.sin(canon_angle) * 10 / 4
                ]
        new_particle = Particle(particle_pos, velocity, True)
        particles.append(new_particle)
        screen_shake_timer = 0.1

    click = False
    k_pressed = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_k:
                k_pressed = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                click = True
                click_pos = (mx, my)
                print(click_pos)
                can_add_new_particle = True

    if screen_shake_timer > 0:
        scaled_display = pygame.transform.scale(display, window.get_size())
        window.blit(scaled_display, (randint(-2, 2), randint(-2, 2)))
    else:
        pygame.transform.scale(display, window.get_size(), window)

    pygame.display.update()
    clock.tick()
