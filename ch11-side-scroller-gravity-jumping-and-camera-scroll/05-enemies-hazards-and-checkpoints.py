class PatrollingEnemy(Entity):
    def __init__(self, x, y, patrol_left, patrol_right, assets):
        image = assets.placeholder_image((26, 26), (200, 60, 60))
        super().__init__(image, x, y)
        self.velocity.x = 70.0
        self.patrol_left = patrol_left
        self.patrol_right = patrol_right

    def update(self, dt):
        super().update(dt)
        if self.rect.left <= self.patrol_left:
            self.velocity.x = abs(self.velocity.x)
        elif self.rect.right >= self.patrol_right:
            self.velocity.x = -abs(self.velocity.x)
