def update_tick(self):
    self.snake.move()

    if self.snake.head == self.food:
        self.snake.grow(1)
        self.food = spawn_food(self.snake.body)
        self.score += 10
        self.eat_sound.play()

    if self.check_collision():
        self.app.states.transition_to("game_over")

def check_collision(self):
    head_col, head_row = self.snake.head
    out_of_bounds = not (0 <= head_col < GRID_WIDTH and 0 <= head_row < GRID_HEIGHT)
    self_collision = self.snake.head in self.snake.body[1:]
    return out_of_bounds or self_collision
