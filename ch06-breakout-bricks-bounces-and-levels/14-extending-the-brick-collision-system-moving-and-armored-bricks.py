class MovingBrick(Brick):
    def __init__(self, x, y, color, points, assets, patrol_range=40):
        super().__init__(x, y, color, points, assets)
        self.velocity.x = 30.0
        self.origin_x = x
        self.patrol_range = patrol_range

    def update(self, dt):
        super().update(dt)
        if abs(self.rect.centerx - self.origin_x) > self.patrol_range:
            self.velocity.x *= -1
