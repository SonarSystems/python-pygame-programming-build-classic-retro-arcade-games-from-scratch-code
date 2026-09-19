import pygame

import random

POWERUP_CHANCE = 0.12
POWERUP_TYPES = ["widen", "slow", "multiball"]


class PowerUp(Entity):
    def __init__(self, x, y, kind, assets):
        color = {"widen": (80, 160, 240), "slow": (160, 80, 240),
                  "multiball": (240, 160, 80)}[kind]
        image = assets.placeholder_image((22, 22), color)
        super().__init__(image, x, y)
        self.kind = kind
        self.velocity = pygame.Vector2(0, 140)


def maybe_spawn_powerup(brick, assets):
    if random.random() < POWERUP_CHANCE:
        kind = random.choice(POWERUP_TYPES)
        return PowerUp(brick.rect.centerx, brick.rect.centery, kind, assets)
    return None
