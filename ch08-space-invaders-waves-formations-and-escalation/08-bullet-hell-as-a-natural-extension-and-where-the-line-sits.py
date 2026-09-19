import pygame

import math


def spawn_spiral_pattern(origin, bullet_count, spiral_speed, assets):
    """Fires bullets in an expanding spiral, a classic bullet-hell
    pattern — each bullet's initial angle is offset from the last by a
    fixed amount, producing a rotating arm of projectiles."""
    bullets = []
    for i in range(bullet_count):
        angle = (i / bullet_count) * 2 * math.pi * 3  # three full rotations
        velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * spiral_speed
        bullet = Bullet(origin[0], origin[1], velocity.y, (240, 90, 200), assets)
        bullet.velocity.x = velocity.x  # Bullet's own __init__ only sets y
        bullets.append(bullet)
    return bullets
