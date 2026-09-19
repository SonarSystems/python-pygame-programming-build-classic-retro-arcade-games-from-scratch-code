def grid_to_pixels(grid_pos):
    col, row = grid_pos
    return (col * GRID_SIZE, row * GRID_SIZE)
