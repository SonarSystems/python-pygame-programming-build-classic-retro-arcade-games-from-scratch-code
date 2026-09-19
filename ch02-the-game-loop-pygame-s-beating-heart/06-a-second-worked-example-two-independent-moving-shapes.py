import math

import pygame

from engine.game_loop import GameLoop


class OrbitingDot:
    def __init__(self):
        self.angle = 0.0
        self.radius = 150
        self.center = pygame.Vector2(400, 300)
        self.angular_speed = 2.2  # radians per second

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.angle += self.angular_speed * dt

    @property
    def position(self):
        x = self.center.x + math.cos(self.angle) * self.radius
        y = self.center.y + math.sin(self.angle) * self.radius
        return (x, y)


class PulsingSquare:
    def __init__(self):
        self.time = 0.0

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.time += dt

    @property
    def size(self):
        return 30 + math.sin(self.time * 3) * 10


class TwoShapesScene:
    def __init__(self):
        self.dot = OrbitingDot()
        self.square = PulsingSquare()

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.dot.update(dt)
        self.square.update(dt)

    def draw(self, surface):
        surface.fill((20, 20, 30))
        pygame.draw.circle(surface, (240, 200, 40), self.dot.position, 10)
        size = self.square.size
        rect = pygame.Rect(0, 0, size, size)
        rect.center = (400, 300)
        pygame.draw.rect(surface, (80, 200, 120), rect)


if __name__ == "__main__":
    loop = GameLoop(800, 600, "Two Independent Shapes")
    loop.set_scene(TwoShapesScene())
    loop.run()
