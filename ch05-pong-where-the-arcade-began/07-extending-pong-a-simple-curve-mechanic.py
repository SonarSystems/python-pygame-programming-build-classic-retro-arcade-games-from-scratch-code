def bounce_off_paddle_with_curve(self, paddle_rect, paddle_velocity):
    offset = (self.rect.centery - paddle_rect.centery) / (paddle_rect.height / 2)
    offset = max(-1.0, min(1.0, offset))

    direction = 1 if self.velocity.x < 0 else -1
    self.speed = min(self.speed + BALL_SPEED_INCREMENT, BALL_MAX_SPEED)

    new_velocity = pygame.Vector2(direction, offset * 0.9)
    if new_velocity.length_squared() == 0:
        new_velocity = pygame.Vector2(direction, 0.01)
    self.velocity = new_velocity.normalize() * self.speed

    # A moving paddle imparts a small amount of extra curve, applied as
    # continuous drift over the ball's subsequent flight rather than an
    # instant direction change, so it reads as "spin" rather than a snap.
    self.spin = paddle_velocity.y * 0.15

def update(self, dt):
    super().update(dt)
    if hasattr(self, "spin") and abs(self.spin) > 1:
        self.velocity.y += self.spin * dt
        self.spin *= max(0.0, 1.0 - 2.0 * dt)  # spin decays over time
    # ... existing wall-bounce logic ...
