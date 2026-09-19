class UFO(Entity):
    def __init__(self, x, y, player, assets):
        image = assets.placeholder_image((34, 18), (200, 90, 200))
        super().__init__(image, x, y)
        self.player = player
        self.velocity = pygame.Vector2(random.choice([-1, 1]) * 90, 0)
        self.fire_cooldown = 1.6

    def update(self, dt):
        super().update(dt)
        wrap_position(self, 800, 600)
        self.fire_cooldown -= dt

    def maybe_fire(self, assets):
        if self.fire_cooldown > 0:
            return None
        self.fire_cooldown = 1.6
        direction = (pygame.Vector2(self.player.rect.center) -
                     pygame.Vector2(self.rect.center))
        if direction.length_squared() == 0:
            return None
        direction = direction.normalize()
        bullet = Bullet(self.rect.centerx, self.rect.centery,
                        direction.y * 260, (200, 90, 200), assets)
        bullet.velocity = direction * 260
        return bullet
