class LayeredScene(Scene):
    def __init__(self):
        super().__init__()
        self.background_sprites = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()  # gameplay layer
        self.ui_sprites = pygame.sprite.Group()

    def update(self, dt):
        self.background_sprites.update(dt)
        self.sprites.update(dt)
        self.ui_sprites.update(dt)

    def draw(self, surface):
        surface.fill((20, 20, 30))
        self.background_sprites.draw(surface)
        self.sprites.draw(surface)
        self.ui_sprites.draw(surface)
