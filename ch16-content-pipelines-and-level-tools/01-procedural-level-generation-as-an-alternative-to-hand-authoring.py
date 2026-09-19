import random


def generate_random_walk_level(width, height, steps):
    """Carves a connected, winding path of floor tiles through an
    initially solid grid, starting from the center and taking random
    steps — a simple but effective procedural level generation
    technique for creating a connected, walkable layout."""
    grid = [["#" for _ in range(width)] for _ in range(height)]
    x, y = width // 2, height // 2
    grid[y][x] = "."

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for _ in range(steps):
        dx, dy = random.choice(directions)
        new_x = max(1, min(width - 2, x + dx))
        new_y = max(1, min(height - 2, y + dy))
        x, y = new_x, new_y
        grid[y][x] = "."

    grid[height // 2][width // 2] = "P"  # player start, at the origin
    return ["".join(row) for row in grid]
