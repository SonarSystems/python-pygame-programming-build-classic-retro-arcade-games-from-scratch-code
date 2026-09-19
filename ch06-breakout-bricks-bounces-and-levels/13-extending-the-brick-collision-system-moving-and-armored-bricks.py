class ArmoredBrick(Brick):
    def __init__(self, x, y, assets):
        self.hits_remaining = 3
        self.colors = [(200, 60, 60), (220, 120, 60), (230, 180, 60)]
        super().__init__(x, y, self.colors[0], 40, assets)

    def take_hit(self, assets):
        self.hits_remaining -= 1
        if self.hits_remaining <= 0:
            return True  # destroyed
        color = self.colors[3 - self.hits_remaining]
        self.image = assets.placeholder_image((BRICK_WIDTH, BRICK_HEIGHT), color)
        return False
