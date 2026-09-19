class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((16, 16))
        self.image.fill((240, 240, 240))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(180, -180)  # pixels per second

    def update(self, dt):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt
