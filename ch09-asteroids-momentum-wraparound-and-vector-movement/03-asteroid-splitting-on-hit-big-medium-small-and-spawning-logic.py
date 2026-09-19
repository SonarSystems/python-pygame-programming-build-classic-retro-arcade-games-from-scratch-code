import pygame
import math

import random

ASTEROID_SIZES = {"large": (48, 2), "medium": (28, 1), "small": (16, 0)}
NEXT_SIZE = {"large": "medium", "medium": "small", "small": None}


class Asteroid(Entity):
    def __init__(self, x, y, size, assets):
        radius, self.points_value = ASTEROID_SIZES[size]
        # A rough polygon rendered onto a transparent surface reads as far
        # more "asteroid-like" than a plain circle or square would.
        image = self._build_shape(radius, assets)
        super().__init__(image, x, y)
        self.size = size
        angle = random.uniform(0, 360)
        speed = random.uniform(40, 110)
        radians = math.radians(angle)
        self.velocity = pygame.Vector2(math.cos(radians), math.sin(radians)) * speed
        self.rotation = random.uniform(-60, 60)  # degrees per second, purely visual
        self.visual_angle = 0.0

    def _build_shape(self, radius, assets):
        surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        points = []
        for i in range(9):
            angle = (i / 9) * 2 * math.pi
            wobble = random.uniform(0.75, 1.0)
            px = radius + math.cos(angle) * radius * wobble
            py = radius + math.sin(angle) * radius * wobble
            points.append((px, py))
        pygame.draw.polygon(surface, (170, 170, 170), points, width=2)
        return surface

    def update(self, dt):
        super().update(dt)
        self.visual_angle += self.rotation * dt
        wrap_position(self, 800, 600)


def split_asteroid(asteroid, assets):
    next_size = NEXT_SIZE[asteroid.size]
    fragments = []
    if next_size is not None:
        for _ in range(2):
            fragments.append(Asteroid(asteroid.rect.centerx, asteroid.rect.centery,
                                       next_size, assets))
    return fragments
