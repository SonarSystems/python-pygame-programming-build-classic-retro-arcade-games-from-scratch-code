import math

import pygame

from engine.entity import Entity

THRUST_ACCELERATION = 320.0  # pixels per second^2
ROTATION_SPEED = 220.0  # degrees per second
MAX_SPEED = 380.0
DRAG = 0.35  # fraction of velocity lost per second, simulating friction


class Ship(Entity):
    def __init__(self, x, y, assets):
        image = assets.placeholder_image((30, 30), (220, 220, 220))
        super().__init__(image, x, y)
        self.angle = 0.0  # degrees, 0 = pointing up
        self.thrusting = False

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= ROTATION_SPEED * dt
        if keys[pygame.K_RIGHT]:
            self.angle += ROTATION_SPEED * dt

        self.thrusting = keys[pygame.K_UP]
        if self.thrusting:
            radians = math.radians(self.angle - 90)
            thrust_vector = pygame.Vector2(math.cos(radians), math.sin(radians))
            self.velocity += thrust_vector * THRUST_ACCELERATION * dt

        # Drag: without this, the ship would accelerate forever and never
        # slow down, which feels uncontrollable rather than "floaty."
        self.velocity *= max(0.0, 1.0 - DRAG * dt)

        if self.velocity.length() > MAX_SPEED:
            self.velocity.scale_to_length(MAX_SPEED)

        super().update(dt)
