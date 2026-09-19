from engine.state_machine import StateMachine

GHOST_SPEED = 108.0
FRIGHTENED_DURATION = 7.0


class Ghost(Entity):
    def __init__(self, col, row, maze, color, scatter_corner, assets):
        image = assets.placeholder_image((TILE_SIZE - 6, TILE_SIZE - 6), color)
        x, y = maze.tile_center_pixels(col, row)
        super().__init__(image, x, y)
        self.maze = maze
        self.direction = pygame.Vector2(1, 0)
        self.states = StateMachine("scatter")
        self.frightened_timer = 0.0
        self.base_color = color
        self.scatter_corner = scatter_corner

    def frighten(self):
        self.states.transition_to("frightened")
        self.frightened_timer = FRIGHTENED_DURATION

    def update(self, dt, pacman):
        if self.states.state == "frightened":
            self.frightened_timer -= dt
            if self.frightened_timer <= 0:
                self.states.transition_to("chase")

        if self._at_tile_center():
            self._choose_direction(pacman)

        speed = GHOST_SPEED * (0.55 if self.states.state == "frightened" else 1.0)
        self.rect.x += self.direction.x * speed * dt
        self.rect.y += self.direction.y * speed * dt

    def _at_tile_center(self):
        col, row = self._current_tile()
        cx, cy = self.maze.tile_center_pixels(col, row)
        return abs(self.rect.centerx - cx) < 3 and abs(self.rect.centery - cy) < 3

    def _current_tile(self):
        return (self.rect.centerx // TILE_SIZE, self.rect.centery // TILE_SIZE)
