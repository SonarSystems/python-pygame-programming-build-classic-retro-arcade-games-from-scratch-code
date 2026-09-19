import random

BALL_SIZE = 16
BALL_START_SPEED = 260.0
BALL_SPEED_INCREMENT = 18.0
BALL_MAX_SPEED = 620.0


class Ball(Entity):
    def __init__(self, assets):
        image = assets.placeholder_image((BALL_SIZE, BALL_SIZE), (240, 200, 40))
        super().__init__(image, WIDTH // 2, HEIGHT // 2)
        self.speed = BALL_START_SPEED
        self.reset(direction=random.choice([-1, 1]))

    def reset(self, direction):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = BALL_START_SPEED
        angle = random.uniform(-0.35, 0.35)  # radians, a mild starting angle
        self.velocity = pygame.Vector2(direction, angle).normalize() * self.speed

    def update(self, dt):
        super().update(dt)
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity.y *= -1
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity.y *= -1

    def bounce_off_paddle(self, paddle_rect):
        # How far from the paddle's center the ball hit, from -1.0 (top
        # edge) to 1.0 (bottom edge), controls the resulting angle —
        # exactly the "aim with where you hit it" feel the original had.
        offset = (self.rect.centery - paddle_rect.centery) / (paddle_rect.height / 2)
        offset = max(-1.0, min(1.0, offset))

        direction = 1 if self.velocity.x < 0 else -1
        self.speed = min(self.speed + BALL_SPEED_INCREMENT, BALL_MAX_SPEED)

        new_velocity = pygame.Vector2(direction, offset * 0.9)
        if new_velocity.length_squared() == 0:
            new_velocity = pygame.Vector2(direction, 0.01)
        self.velocity = new_velocity.normalize() * self.speed
