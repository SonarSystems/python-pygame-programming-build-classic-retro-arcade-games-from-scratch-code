class BrickFragment:
    def __init__(self, x, y, color):
        self.pos = pygame.Vector2(x, y)
        angle = random.uniform(0, 6.28)
        speed = random.uniform(80, 220)
        self.velocity = pygame.Vector2(speed, 0).rotate_rad(angle)
        self.lifetime = 0.4
        self.age = 0.0
        self.color = color

    def update(self, dt):
        self.pos += self.velocity * dt
        self.velocity.y += 400 * dt  # a light gravity pull
        self.age += dt

    @property
    def alive(self):
        return self.age < self.lifetime

    def draw(self, surface):
        alpha_fraction = 1.0 - (self.age / self.lifetime)
        size = max(1, int(6 * alpha_fraction))
        pygame.draw.rect(surface, self.color,
                          (self.pos.x, self.pos.y, size, size))
