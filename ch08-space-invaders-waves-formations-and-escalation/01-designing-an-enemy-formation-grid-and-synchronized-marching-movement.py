import pygame

ENEMY_COLS, ENEMY_ROWS = 8, 4
ENEMY_SPACING_X, ENEMY_SPACING_Y = 56, 44
ENEMY_START_X, ENEMY_START_Y = 80, 60


class Formation:
    def __init__(self, assets):
        self.offset = pygame.Vector2(0, 0)
        self.direction = 1  # 1 = moving right, -1 = moving left
        self.speed = 40.0  # pixels per second, increases as enemies die
        self.drop_amount = 24
        self.enemies = pygame.sprite.Group()
        self._build(assets)

    def _build(self, assets):
        for row in range(ENEMY_ROWS):
            for col in range(ENEMY_COLS):
                slot_x = ENEMY_START_X + col * ENEMY_SPACING_X
                slot_y = ENEMY_START_Y + row * ENEMY_SPACING_Y
                point_value = 30 if row == 0 else (20 if row < 3 else 10)
                enemy = Enemy(slot_x, slot_y, point_value, assets)
                self.enemies.add(enemy)

    def update(self, dt):
        self.offset.x += self.speed * self.direction * dt

        edge_hit = False
        for enemy in self.enemies:
            actual_x = enemy.slot_x + self.offset.x
            if actual_x <= 20 or actual_x >= 780:
                edge_hit = True
                break

        if edge_hit:
            self.direction *= -1
            self.offset.y += self.drop_amount

        for enemy in self.enemies:
            enemy.rect.x = enemy.slot_x + self.offset.x
            enemy.rect.y = enemy.slot_y + self.offset.y
