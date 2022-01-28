import pygame

from random import randint


class Camera:
    def __init__(self, engine):
        self.engine = engine
        self.screen_shake_timer = 0
        self.offset = [0, 0]
        self.shake_impact = 3

    def render(self):
        display = self.engine.display
        window = self.engine.window
        if any(self.offset):
            display_scaled = pygame.transform.scale(display, window.get_size())
            window.blit(display_scaled, self.offset)
        else:
            pygame.transform.scale(display, window.get_size(), window)

    def set_screen_shake(self, time):
        self.screen_shake_timer += time

    def set_shake_impact(self, impact):
        self.shake_impact = impact

    def update(self, dt):
        self.screen_shake_timer = max(self.screen_shake_timer - dt, 0)
        if self.screen_shake_timer:
            x_offset = randint(-self.shake_impact, self.shake_impact)
            y_offset = randint(-self.shake_impact, self.shake_impact)
            self.offset = [x_offset, y_offset]
