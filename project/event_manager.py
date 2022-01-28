import pygame
import sys

from pygame.locals import *
from config import config


class EventManager:
    def __init__(self):
        self.mouse = {
                'click': False,
                'left_hold': False
                }
        self.clicked_keys = {
                'k': False
                }

        self.screen_x_ratio = config['window']['window_size'][0] / config['window']['display_size'][0]
        self.screen_y_ratio = config['window']['window_size'][1] / config['window']['display_size'][1]

    def reset_events(self):
        for key in self.clicked_keys:
            self.clicked_keys[key] = False
        self.mouse['click'] = False

    def update(self):

        self.reset_events()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_k:
                    self.clicked_keys['k'] = True

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse['click'] = True
                    self.mouse['left_hold'] = True

            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse['click'] = False
                    self.mouse['left_hold'] = False

    def mouse_pos(self):
        mx, my = pygame.mouse.get_pos()
        mx /= self.screen_x_ratio
        my /= self.screen_y_ratio
        return mx, my
