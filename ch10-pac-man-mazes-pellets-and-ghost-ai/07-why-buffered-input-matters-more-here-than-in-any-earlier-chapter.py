import pygame

def update_unbuffered(self, dt):
    if self._at_tile_center():
        keys = pygame.key.get_pressed()
        col, row = self._current_tile()
        # Check whichever direction key is currently held, right now,
        # at the exact instant the player reaches this tile's center.
        if keys[pygame.K_RIGHT] and not self.maze.is_wall(col + 1, row):
            self.direction = pygame.Vector2(1, 0)
        elif keys[pygame.K_DOWN] and not self.maze.is_wall(col, row + 1):
            self.direction = pygame.Vector2(0, 1)
        # ... etc for left and up ...
    self.rect.x += self.direction.x * self.speed * dt
    self.rect.y += self.direction.y * self.speed * dt
