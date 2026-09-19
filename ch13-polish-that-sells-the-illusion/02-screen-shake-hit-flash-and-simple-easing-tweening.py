class ScreenShake:
    def __init__(self):
        self.trauma = 0.0
        self.decay_rate = 2.4

    def add_trauma(self, amount):
        self.trauma = min(1.0, self.trauma + amount)

    def update(self, dt):
        self.trauma = max(0.0, self.trauma - self.decay_rate * dt)

    def offset(self):
        if self.trauma <= 0:
            return pygame.Vector2(0, 0)
        magnitude = self.trauma ** 2  # squaring makes small shakes gentler
        return pygame.Vector2(
            random.uniform(-1, 1) * magnitude * 12,
            random.uniform(-1, 1) * magnitude * 12,
        )
