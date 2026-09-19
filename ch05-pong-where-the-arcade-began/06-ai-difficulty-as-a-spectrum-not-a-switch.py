DIFFICULTY_PRESETS = {
    "easy": {"speed_multiplier": 0.60, "reaction_margin": 40},
    "medium": {"speed_multiplier": 0.82, "reaction_margin": 12},
    "hard": {"speed_multiplier": 0.95, "reaction_margin": 4},
}


class AIPaddle(Paddle):
    def __init__(self, x, y, assets, ball, difficulty="medium"):
        super().__init__(x, y, assets)
        self.ball = ball
        preset = DIFFICULTY_PRESETS[difficulty]
        self.speed_multiplier = preset["speed_multiplier"]
        self.reaction_margin = preset["reaction_margin"]

    def update(self, dt):
        target_y = self.ball.rect.centery
        if self.rect.centery < target_y - self.reaction_margin:
            self.velocity.y = PADDLE_SPEED * self.speed_multiplier
        elif self.rect.centery > target_y + self.reaction_margin:
            self.velocity.y = -PADDLE_SPEED * self.speed_multiplier
        else:
            self.velocity.y = 0
        super().update(dt)
        self.clamp_to_screen()
