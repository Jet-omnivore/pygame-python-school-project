# ghatiya jatan
import math
import pygame


class Canon:
    def __init__(self, world, pos):
        self.world = world

        self.angle = 0
        self.base_img = self.world.assest.assests['img']['base']

        self.base_pos = [pos[0] - self.base_half_width, pos[1]]
        self.shooter_pos = [self.base_pos[0] + self.base_half_width, self.base_pos[1] - self.shooter_half_height]


    @property
    def shooter_img(self):
        img = self.world.assest.assests['img']['shooter'].copy()
        img = pygame.transform.rotate(img, self.angle)
        return img

    @property
    def base_half_width(self):
        return self.base_img.get_width() / 2

    @property
    def base_half_height(self):
        return self.base_img.get_height() / 2

    @property
    def shooter_half_width(self):
        return self.shooter_img.get_width() / 2

    @property
    def shooter_half_height(self):
        return self.shooter_img.get_height() / 2

    def render(self, surf):
        surf.blit(self.base_img, self.base_pos)
        self.render_angle()

        shooter_img = self.shooter_img
        zipped_size = zip(self.shooter_pos, shooter_img.get_size())
        shooter_pos = [x - y // 2 for x, y in zipped_size]
        surf.blit(self.shooter_img, shooter_pos)

    def update(self):
        mx, my = self.world.engine.event.mouse_pos()

        difference = -(my - self.shooter_pos[1]), mx - self.shooter_pos[0]
        angle = math.atan2(*difference)
        deg_angle = math.degrees(angle)
        self.angle = min(max(deg_angle, 0), 90)

        k_clicked = self.world.engine.event.clicked_keys['k']
        mouse_clicked = self.world.engine.event.mouse['click']
        if mouse_clicked or k_clicked:
            self.shoot()

    def shoot(self):
        self.world.engine.camera.set_screen_shake(0.6)
        mx, my = self.world.engine.event.mouse_pos()
        px, py = self.shooter_pos
        angle = math.radians(-(self.angle ))# - 2.5))
        velocity = math.cos(angle) * 60, math.sin(angle) * 60
        self.world.projectile_manager.add_projectile([px, py], velocity)

    def render_angle(self):
        self.world.engine.font.render(f"{int(self.angle)}", [50, 50])
