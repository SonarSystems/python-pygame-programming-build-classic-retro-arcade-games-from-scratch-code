BRICK_WIDTH, BRICK_HEIGHT = 60, 22
BRICK_GAP = 4
BRICK_TOP_MARGIN = 60


class Brick(Entity):
    def __init__(self, x, y, color, points, assets):
        image = assets.placeholder_image((BRICK_WIDTH, BRICK_HEIGHT), color)
        super().__init__(image, x, y)
        self.points = points


def build_level(level_rows, assets):
    bricks = pygame.sprite.Group()
    for row_index, row in enumerate(level_rows):
        for col_index, char in enumerate(row):
            if char == ".":
                continue
            x = col_index * (BRICK_WIDTH + BRICK_GAP) + BRICK_WIDTH // 2 + 20
            y = row_index * (BRICK_HEIGHT + BRICK_GAP) + BRICK_TOP_MARGIN
            color = BRICK_COLORS[char]
            points = {"R": 30, "O": 20, "Y": 15, "G": 10}[char]
            bricks.add(Brick(x, y, color, points, assets))
    return bricks
