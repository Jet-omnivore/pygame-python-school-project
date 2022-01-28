from entities.projectiles import ProjectileManager
from entities.canon import Canon
from tile_map import TileMap
from assest import Assest


class World:
    def __init__(self, engine):
        self.engine = engine
        self.projectile_manager = ProjectileManager(self)
        self.tilemap = TileMap(self)
        self.assest = Assest()

        self.canon = Canon(self, (40, 240))

    def render(self):
        self.tilemap.render(self.engine.display)
        self.canon.render(self.engine.display)

    def update(self):
        self.update_enities()
        self.render()

    def update_enities(self):
        self.canon.update()
        self.projectile_manager.update()
