import math

from dataclasses import dataclass


@dataclass
class vec2:
    x: float = 0.0
    y: float = 0.0

    @property
    def mag(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    @property
    def angle(self) -> float:
        """returns angle in radians"""
        math.atan2(self.y, self.x)

    @property
    def deg_angle(self) -> float:
        """returns angle in degrees"""
        math.degrees(self.angle)

    def copy(self):
        return vec2(self.x, self.y)

    def __iter__(self):
        return [self.x, self.y]
