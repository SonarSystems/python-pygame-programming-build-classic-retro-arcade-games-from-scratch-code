import pygame

def _choose_direction(self, pacman):
    col, row = self._current_tile()
    target = self._current_target(pacman)

    candidates = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        # Ghosts traditionally never reverse direction except when
        # frightened state begins — this keeps movement feeling
        # decisive rather than twitchy.
        if (dx, dy) == (-self.direction.x, -self.direction.y):
            continue
        next_col, next_row = col + dx, row + dy
        if not self.maze.is_wall(next_col, next_row):
            candidates.append((dx, dy, next_col, next_row))

    if not candidates:
        self.direction *= -1
        return

    def distance_to_target(candidate):
        _, _, ncol, nrow = candidate
        return (ncol - target[0]) ** 2 + (nrow - target[1]) ** 2

    if self.states.state == "frightened":
        best = max(candidates, key=distance_to_target)
    else:
        best = min(candidates, key=distance_to_target)

    self.direction = pygame.Vector2(best[0], best[1])

def _current_target(self, pacman):
    if self.states.state == "scatter":
        return self.scatter_corner
    pac_col, pac_row = pacman._current_tile()
    return (pac_col, pac_row)
