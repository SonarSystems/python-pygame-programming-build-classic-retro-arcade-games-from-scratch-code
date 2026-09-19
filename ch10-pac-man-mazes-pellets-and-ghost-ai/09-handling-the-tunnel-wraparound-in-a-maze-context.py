TUNNEL_ROW = 4  # the row index in MAZE_MAP that acts as a tunnel

def apply_tunnel_wrap(entity, maze):
    col, row = entity._current_tile()
    if row != TUNNEL_ROW:
        return
    if entity.rect.centerx < 0:
        entity.rect.centerx = maze.width * TILE_SIZE
    elif entity.rect.centerx > maze.width * TILE_SIZE:
        entity.rect.centerx = 0
