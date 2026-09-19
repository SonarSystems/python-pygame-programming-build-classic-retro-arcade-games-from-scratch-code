def update_difficulty(formation):
    remaining = len(formation.enemies)
    total = ENEMY_COLS * ENEMY_ROWS
    fraction_remaining = remaining / total
    # Speed roughly doubles as the formation thins from full to nearly empty.
    formation.speed = 40.0 + (1.0 - fraction_remaining) * 90.0
