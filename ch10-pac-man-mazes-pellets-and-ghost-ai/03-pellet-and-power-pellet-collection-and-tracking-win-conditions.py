class Pacman(Entity):
    def __init__(self, col, row, maze, assets):
        image = assets.placeholder_image((TILE_SIZE - 4, TILE_SIZE - 4), (240, 220, 40))
        x, y = maze.tile_center_pixels(col, row)
        super().__init__(image, x, y)
        self.maze = maze
        self.direction = pygame.Vector2(0, 0)
        self.next_direction = pygame.Vector2(0, 0)
        self.speed = 130.0

    def set_next_direction(self, dx, dy):
        self.next_direction = pygame.Vector2(dx, dy)

    def _at_tile_center(self):
        col, row = self._current_tile()
        cx, cy = self.maze.tile_center_pixels(col, row)
        return abs(self.rect.centerx - cx) < 3 and abs(self.rect.centery - cy) < 3

    def _current_tile(self):
        return (self.rect.centerx // TILE_SIZE, self.rect.centery // TILE_SIZE)

    def update(self, dt):
        if self._at_tile_center():
            col, row = self._current_tile()
            next_col = col + int(self.next_direction.x)
            next_row = row + int(self.next_direction.y)
            if not self.maze.is_wall(next_col, next_row):
                self.direction = self.next_direction

            forward_col = col + int(self.direction.x)
            forward_row = row + int(self.direction.y)
            if self.maze.is_wall(forward_col, forward_row):
                self.direction = pygame.Vector2(0, 0)

        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt
