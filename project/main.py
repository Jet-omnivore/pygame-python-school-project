import pygame

from config import config
from world import World
from event_manager import EventManager
from font import Font
from camera import Camera


def draw_to_screen(surf, window):
    pygame.transform.scale(surf, window.get_size(), window)


class Project:
    def __init__(self):
        pygame.init()

        window_size = config['window']['window_size']
        self.window = pygame.display.set_mode(window_size, pygame.SCALED)
        self.display = pygame.Surface(config['window']['display_size'])

        self.dt = 0
        self.clock = pygame.time.Clock()

        self.world = World(self)
        self.camera = Camera(self)
        self.event = EventManager()
        self.font = Font(self)

    def run(self):
        while True:
            self.display.fill(config['window']['background_color'])
            self.update()
            self.render()

    def render(self):
        self.camera.render()
        pygame.display.update()

    def update(self):
        self.camera.update(self.dt)
        self.event.update()
        self.world.update()
        self.dt = self.clock.tick()
        self.dt *= 0.01


if __name__ == "__main__":
    Project().run()
