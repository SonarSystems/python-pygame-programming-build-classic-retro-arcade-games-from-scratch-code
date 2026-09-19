import random

ENEMY_FIRE_CHANCE_PER_SECOND = 0.6


def front_row_enemies(enemies):
    """One enemy per column: whichever is lowest (closest to the player)."""
    columns = {}
    for enemy in enemies:
        col = enemy.slot_x
        if col not in columns or enemy.rect.y > columns[col].rect.y:
            columns[col] = enemy
    return list(columns.values())


def maybe_enemy_fire(formation, assets, dt):
    eligible = front_row_enemies(formation.enemies)
    if not eligible:
        return None
    chance_this_frame = ENEMY_FIRE_CHANCE_PER_SECOND * dt
    if random.random() < chance_this_frame:
        shooter = random.choice(eligible)
        return Bullet(shooter.rect.centerx, shooter.rect.bottom, 220, (240, 90, 90), assets)
    return None
