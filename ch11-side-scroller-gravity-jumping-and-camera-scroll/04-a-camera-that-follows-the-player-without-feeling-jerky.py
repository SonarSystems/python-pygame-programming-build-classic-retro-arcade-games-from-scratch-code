import pygame

class Camera:
    def __init__(self, width, height, level_width, level_height):
        self.offset = pygame.Vector2(0, 0)
        self.width = width
        self.height = height
        self.level_width = level_width
        self.level_height = level_height
        self.smoothing = 6.0  # higher = snappier, lower = lazier

    def update(self, dt, target_rect):
        desired_x = target_rect.centerx - self.width / 2
        desired_y = target_rect.centery - self.height / 2

        desired_x = max(0, min(desired_x, self.level_width - self.width))
        desired_y = max(0, min(desired_y, self.level_height - self.height))

        self.offset.x += (desired_x - self.offset.x) * min(1.0, self.smoothing * dt)
        self.offset.y += (desired_y - self.offset.y) * min(1.0, self.smoothing * dt)

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)
