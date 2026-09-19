import pygame

from engine.entity import Entity

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 14, 90
PADDLE_SPEED = 380.0  # pixels per second


class Paddle(Entity):
    def __init__(self, x, y, assets):
        image = assets.placeholder_image((PADDLE_WIDTH, PADDLE_HEIGHT),
                                          (230, 230, 230))
        super().__init__(image, x, y)

    def clamp_to_screen(self):
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(HEIGHT, self.rect.bottom)


class PlayerPaddle(Paddle):
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.velocity.y = -PADDLE_SPEED
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.velocity.y = PADDLE_SPEED
        else:
            self.velocity.y = 0
        super().update(dt)
        self.clamp_to_screen()


class AIPaddle(Paddle):
    def __init__(self, x, y, assets, ball):
        super().__init__(x, y, assets)
        self.ball = ball
        self.reaction_margin = 12  # pixels of "dead zone" so the AI isn't perfect

    def update(self, dt):
        target_y = self.ball.rect.centery
        if self.rect.centery < target_y - self.reaction_margin:
            self.velocity.y = PADDLE_SPEED * 0.82
        elif self.rect.centery > target_y + self.reaction_margin:
            self.velocity.y = -PADDLE_SPEED * 0.82
        else:
            self.velocity.y = 0
        super().update(dt)
        self.clamp_to_screen()
