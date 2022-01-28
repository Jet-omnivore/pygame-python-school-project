import pygame

from config import config


class Font:
    def __init__(self, engine):
        font_name, font_size = config['font']['font'], config['font']['size']
        self.font = pygame.font.SysFont(font_name, font_size)
        self.engine = engine

    def render(self, text, pos, color=(255, 255, 255), surf=None):
        if surf is None:
            surf = self.engine.display
        text_surf = self.font.render(text, False, color)
        surf.blit(text_surf, pos)
