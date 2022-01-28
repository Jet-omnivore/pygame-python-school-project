import pygame

from config import config
from math import ceil
from enum import Enum, auto


class Tiles(Enum):
    RECT = auto()
    IMG = auto()


class TileMap:
    def __init__(self, world):
        self.map = {}
        self.rect_tile_size = 15
        self.add_ground()
        self.world = world

    def add_ground(self):
        tile_size = self.rect_tile_size
        x_step = ceil(config['window']['display_size'][0] / tile_size)
        y_step = ceil(config['window']['display_size'][1] / tile_size)

        for x in range(x_step):
            for y in range(y_step):
                if y in [y_step - 1]:
                    tile_pos = (x, y)

                    # [tile_type, color/image id]
                    self.map[tile_pos] = [Tiles.RECT, (255, 0, 0)]

    def render(self, surf):
        tile_size = self.rect_tile_size
        for pos in self.map:
            if self.map[pos][0] is Tiles.RECT:
                tile_size = self.rect_tile_size
                tile_pos = (pos[0] * tile_size, pos[1] * tile_size)
                rect = (*tile_pos, tile_size, tile_size)
                pygame.draw.rect(surf, self.map[pos][1], rect)
