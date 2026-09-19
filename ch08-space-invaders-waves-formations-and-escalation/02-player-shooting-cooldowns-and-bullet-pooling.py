import pygame

class Player(Entity):
    def __init__(self, x, y, assets):
        image = assets.placeholder_image((40, 20), (80, 200, 120))
        super().__init__(image, x, y)
        self.speed = 260.0
        self.cooldown = 0.0
        self.cooldown_duration = 0.4

    def update(self, dt):
        self.cooldown = max(0.0, self.cooldown - dt)
        keys = pygame.key.get_pressed()
        self.velocity.x = 0
        if keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        super().update(dt)
        self.rect.clamp_ip(pygame.Rect(0, 0, 800, 600))

    def can_fire(self):
        return self.cooldown <= 0.0

    def fire(self):
        self.cooldown = self.cooldown_duration


class Bullet(Entity):
    def __init__(self, x, y, velocity_y, color, assets):
        image = assets.placeholder_image((4, 14), color)
        super().__init__(image, x, y)
        self.velocity = pygame.Vector2(0, velocity_y)

    def update(self, dt):
        super().update(dt)
        if self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()
