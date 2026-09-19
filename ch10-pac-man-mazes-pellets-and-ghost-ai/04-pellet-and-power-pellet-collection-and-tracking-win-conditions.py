def check_pellet_collection(self):
    tile = self._current_tile()
    if tile in self.maze.pellets:
        self.maze.pellets.discard(tile)
        self.score += 10
        return "pellet"
    if tile in self.maze.power_pellets:
        self.maze.power_pellets.discard(tile)
        self.score += 50
        return "power_pellet"
    return None
