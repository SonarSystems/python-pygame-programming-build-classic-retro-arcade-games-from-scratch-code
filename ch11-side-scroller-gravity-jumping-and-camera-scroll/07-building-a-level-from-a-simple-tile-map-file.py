LEVEL_1 = [
    "..................",
    "..................",
    "........E.........",
    "####..######......",
    "..................",
    "..P..........C....",
    "##################",
]

TILE_SIZE = 32
# . = empty, # = solid ground, P = player start, E = patrolling enemy,
# C = checkpoint


def build_level(rows, assets):
    solids = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    checkpoints = pygame.sprite.Group()
    player_start = (100, 100)

    for row_index, row in enumerate(rows):
        for col_index, char in enumerate(row):
            x = col_index * TILE_SIZE + TILE_SIZE // 2
            y = row_index * TILE_SIZE + TILE_SIZE // 2
            if char == "#":
                solids.add(SolidTile(x, y, assets))
            elif char == "P":
                player_start = (x, y)
            elif char == "E":
                enemies.add(PatrollingEnemy(x, y, x - 80, x + 80, assets))
            elif char == "C":
                checkpoints.add(Checkpoint(x, y, assets))

    return solids, enemies, checkpoints, player_start
