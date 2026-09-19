class GameSettings:
    def __init__(self):
        self.wrap_walls = False


def check_collision(self):
    head_col, head_row = self.snake.head

    if self.settings.wrap_walls:
        head_col %= GRID_WIDTH
        head_row %= GRID_HEIGHT
        self.snake.body[0] = (head_col, head_row)
        out_of_bounds = False
    else:
        out_of_bounds = not (0 <= head_col < GRID_WIDTH and 0 <= head_row < GRID_HEIGHT)

    self_collision = self.snake.head in self.snake.body[1:]
    return out_of_bounds or self_collision
