class SmoothSnakeRenderer:
    def __init__(self, snake, tick_timer):
        self.snake = snake
        self.tick_timer = tick_timer

    def rendered_positions(self):
        # How far through the current tick interval we are, 0.0 to 1.0.
        progress = self.tick_timer.accumulated / self.tick_timer.interval
        positions = []
        for i, (col, row) in enumerate(self.snake.body):
            if i + 1 < len(self.snake.body):
                prev_col, prev_row = self.snake.body[i + 1]
            else:
                prev_col, prev_row = col, row
            smooth_col = prev_col + (col - prev_col) * progress
            smooth_row = prev_row + (row - prev_row) * progress
            positions.append((smooth_col * GRID_SIZE, smooth_row * GRID_SIZE))
        return positions
