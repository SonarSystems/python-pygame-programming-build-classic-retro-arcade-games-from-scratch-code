import pygame

LASER_COOLDOWN = 0.35
LASER_DURATION = 8.0


class LaserBolt(Entity):
    def __init__(self, x, y, assets):
        image = assets.placeholder_image((3, 16), (240, 80, 80))
        super().__init__(image, x, y)
        self.velocity = pygame.Vector2(0, -420)

    def update(self, dt):
        super().update(dt)
        if self.rect.bottom < 0:
            self.kill()


class Paddle(Entity):
    def __init__(self, x, y, assets):
        # ... existing __init__ body ...
        self.laser_timer = 0.0
        self.laser_cooldown = 0.0

    def activate_laser(self):
        self.laser_timer = LASER_DURATION

    def update_laser(self, dt, keys, laser_bolts, assets):
        if self.laser_timer <= 0:
            return
        self.laser_timer -= dt
        self.laser_cooldown = max(0.0, self.laser_cooldown - dt)
        if keys[pygame.K_SPACE] and self.laser_cooldown <= 0:
            self.laser_cooldown = LASER_COOLDOWN
            laser_bolts.add(LaserBolt(self.rect.left + 6, self.rect.top, assets))
            laser_bolts.add(LaserBolt(self.rect.right - 6, self.rect.top, assets))
