class ZigzagEnemy(Enemy):
    """A rare enemy type that breaks from the formation briefly to dive
    toward the player before rejoining, adding an unpredictable threat
    beyond the formation's otherwise-uniform marching movement."""

    def __init__(self, slot_x, slot_y, point_value, assets):
        super().__init__(slot_x, slot_y, point_value, assets)
        self.diving = False
        self.dive_timer = 0.0

    def maybe_start_dive(self, dt, dive_chance_per_second=0.03):
        if not self.diving and random.random() < dive_chance_per_second * dt:
            self.diving = True
            self.dive_timer = 2.5
            self.velocity = pygame.Vector2(0, 160)

    def update_dive(self, dt):
        if self.diving:
            self.dive_timer -= dt
            self.rect.y += self.velocity.y * dt
            if self.dive_timer <= 0 or self.rect.top > 600:
                self.diving = False
                self.rect.x = self.slot_x
                self.rect.y = self.slot_y
